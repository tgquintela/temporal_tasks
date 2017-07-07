
import numpy as np
import time


class SVM(object):
    """SVM with SGD optimizer.
    """
    def __init__(self, loss='Hinge', batch_size=10, n_epochs=0, learning_rate=0.0001,
                 stop_step=.000001, lambda_par=1., verbose=False, history=True):

        ## Setting loss
        loss_functions = {'hinge': Hinge}
        if type(loss) == str:
            self.lossf = loss_functions[loss.lower()]()
        else:
            self.lossf = loss

        ## Optimizer parameters
        self.optimizer = 'SGD'
        self.n_epochs = n_epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.stop_step = stop_step

        ## Model parameters
        self._reset_model()
        self.lambda_par = lambda_par

        ## Tracking results
        self.last_loss = 1e16
        self.change_loss = 1e16
        self.history = history
        self._reset_history()

    def predict(self, X):
        return np.dot(X, self.w)+self.w0

    def score(self, X, y):
        """Scoring with accuracy measure by default."""
        y_pred = self.predict(X)
        return accuracy(y_pred, y)

    def compute_epoch_measures(self, X_train, y_train, X_test, y_test):
        N_samples = len(X_train)
        testing_phase = (X_test is not None) and (y_test is not None)
        if not testing_phase:
            loss_test = None
            acc_test = None

        # Prediction train
        y_p_train = self.predict(X_train)

        # Hinge loss train
        reg_term = self._regularization()
        lossf_term = self.lossf.loss(y_p_train, y_train)
        losses_epoch = reg_term+lossf_term

        # Change loss
        self.change_loss = self.last_loss-losses_epoch
        self.last_loss = losses_epoch

        # Accuracy train
        train_acc = accuracy(np.sign(y_p_train), y_train)

        if testing_phase:
            # Prediction test
            y_p_test = self.predict(X_test)
            # Hinge loss test
            loss_test = self.lossf.loss(y_p_test, y_test)
            loss_test += reg_term
            #Accuracy test
            acc_test = accuracy(np.sign(y_p_test), y_test)

        # Add to history
        self._add_epoch_to_history(losses_epoch, train_acc,
                                   loss_test, acc_test)
        # Add new epoch to the counter
        self.epoch_learned += 1

    def fit(self, X_train, y_train, X_test=None, y_test=None):
        """"""
        # Setting administrative parameters
        self._reset_history()
        t0 = time.time()
        # Setting general paramaters
        N_samples, n_feats = X_train.shape
        # Initialize model parameters
        self._initialization_weights(n_feats)
        # Setting loop epochs
        keep = True
        i = 0
        while keep:
            # Shuffling data
            data, labels = permut_data(X_train, y_train)
            # Loop over batches
            for x_batch, y_batch in self._batch_generator(data, labels):
                # Batch prediction
                y_batch_pred = self.predict(x_batch)
                # Compute gradient
                gradloss_w, gradloss_w0 =\
                    self.lossf.gradient_loss(y_batch_pred, y_batch, x_batch)
                gradloss_w += self.lambda_par*self.w
                gradloss_w0 += self.lambda_par*self.w0
                # Paramters update
                self.w -= self.learning_rate*gradloss_w
                self.w0 -= self.learning_rate*gradloss_w0
                grad_w_reg, grad_w0_reg = self._gradient_regularization()
                gradloss_w += grad_w_reg
                gradloss_w0 += grad_w0_reg
            # Tracking loss
            self.compute_epoch_measures(X_train, y_train, X_test, y_test)

            # Tracking loop
            i += 1
            keep = stop_condition(self.change_loss, i, self.n_epochs, self.stop_step)
        self.fit_times = time.time()-t0
        return self

    def report_results(self):
        report = "="*25+"\n"
        report += "learning_rate = {}\n"
        report += "regularization = {:.2f}\n"
        report += "batch_size = {}\n"
        report += "="*25+"\n"
        report += "time expended: {:.2f}s\n"
        report += "num. epochs: {}\n"
        report += "best epoch acc: {}\n"
        report += "accuracy train: {:.4f}\n"
        report += "accuracy test: {:.4f}\n"
        report += "="*25+"\n"
        # The criteria of get the accuracy will be the accuracies in the epoch with
        # better test accuracy.
        best_i = np.argmax(self.test_accuracy_history)
        train_accuracy = self.train_accuracy_history[best_i]
        test_accuracy = self.test_accuracy_history[best_i]
        report = report.format(self.learning_rate, self.lambda_par, self.batch_size,
                               self.fit_time, self.epoch_learned, best_i,
                               train_accuracy, test_accuracy)
        print(report)

    def _add_epoch_to_history(self, train_loss, train_accuracy,
                              test_loss=None, test_accuracy=None):
        if self.history:
            self.train_loss_history.append(train_loss)
            self.train_accuracy_history.append(train_accuracy)
            if test_loss is not None:
                self.test_loss_history.append(test_loss)
                self.test_accuracy_history.append(test_accuracy)

    def _reset_history(self):
        self.epoch_learned = 0
        self.fit_time = 0.
        self.train_loss_history = None
        self.test_loss_history = None
        self.train_accuracy_history = None
        self.test_accuracy_history = None
        if self.history:
            self.train_loss_history = []
            self.train_accuracy_history = []
            self.test_loss_history = []
            self.test_accuracy_history = []

    def _reset_model(self):
        self.w = None
        self.w0 = None

    def _initialization_weights(self, n_feats, init_type='gauss'):
        if init_type == 'zeros':
            self.w0 = 0.
            self.w = np.zeros(n_feats)
        elif init_type == 'gauss':
            self.w0 = np.random.randn()
            self.w = np.random.randn(n_feats)

    def _batch_generator(self, data, labels):
        """We can implement here different options to sample batches."""
        N_samples = len(data)
        for init, endit in batch_size_iter(N_samples, self.batch_size):
            x_batch = data[init:endit]
            y_batch = labels[init:endit]
            yield x_batch, y_batch
            
    def _regularization(self):
        """By default it is coded 'L2' but it could be implemented others."""
        return 0.5*(np.dot(self.w, self.w)+self.w0**2)*self.lambda_par

    def _gradient_regularization(self):
        return self.lambda_par*self.w, self.lambda_par*self.w0


class LossFunction(object):
    """General object for loss functions."""
    def __init__(self):
        required_functions = ['loss', 'gradient_loss']
        for req in required_functions:
            assert(req in dir(self))


class Hinge(LossFunction):
    """Loss function for trainning binary linear classifiers with target
    {-1, 1}. It computes the aggregated loss, not the average per sample.
    """

    def __init__(self, threshold=1.0):
        self.threshold = threshold
        super(Hinge, self).__init__()

    def loss(self, y_pred, y_true):
        z = y_pred * y_true
        loss = np.mean((self.threshold - z)*(z <= self.threshold).astype(float))
        return loss

    def gradient_loss(self, y_pred, y, x):
        """Derivation dL/dw. It is separated the output for w and w0.
        """
        z = y_pred * y
        in_margin = (z <= self.threshold).astype(float)

        gradloss_w = -np.dot(y*in_margin, x)
        gradloss_w0 = -np.sum(y*in_margin)

        return gradloss_w, gradloss_w0


def accuracy(y_pred, y_true):
    return np.sum(y_true == y_pred) / float(y_true.shape[0])


def batch_size_iter(data_size, batch_size):
    init = 0
    keep = True
    while keep:
        endit = init+batch_size
        if endit >= data_size:
            endit = data_size
            keep = False
        yield init, endit
        init += batch_size


def stop_condition(loss_change, i, N, stop_step):
    if N != 0:
        if i >= N:
            return False
    if loss_change < stop_step:
        return False
    return True


def permut_data(data, labels=None):
    n_samples = len(data)
    reindices = np.random.permutation(n_samples)
    if labels is None:
        return data[reindices]
    else:
        return data[reindices], labels[reindices]

