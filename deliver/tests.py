import numpy as np
import unittest
from itertools import product

from svm import *


class PermutationDataTest(unittest.TestCase):

    def testpropershape(self):
        data = np.random.random((10, 4))
        labels = np.random.randint(0, 2, 10)*2-1

        data_per = permut_data(data)
        assert(data_per.shape == data.shape)

        data_per, labels_per = permut_data(data, labels)
        assert(data_per.shape == data.shape)
        assert(labels_per.shape == labels.shape)


class StopperTest(unittest.TestCase):

    def test_stopbychange(self):
        N = 0
        i = 10
        loss_change = 0.5

        stop_step = 0.4
        ifkeep = stop_condition(loss_change, i, N, stop_step)
        assert(ifkeep)

        stop_step = 0.6
        ifkeep = stop_condition(loss_change, i, N, stop_step)
        assert(not ifkeep)

    def test_stopbyiter(self):
        loss_change = 0.5
        stop_step = 0.4
        N = 100

        i = 10
        ifkeep = stop_condition(loss_change, i, N, stop_step)
        assert(ifkeep)

        i = 100
        ifkeep = stop_condition(loss_change, i, N, stop_step)
        assert(not ifkeep)


class BatchCreatorTest(unittest.TestCase):

    def test_run_batch_iterator(self):
        data_size = 100
        batch_size = 9
        for init, endit in batch_size_iter(data_size, batch_size):
            assert(init != endit)
            assert(init < endit)
        assert(endit == data_size)

        data_size = 100
        batch_size = 10
        for init, endit in batch_size_iter(data_size, batch_size):
            assert(init != endit)
            assert(init < endit)
        assert(endit == data_size)


class AccuracyFunctionTest(unittest.TestCase):

    def test_order_independency(self):
        n = 10
        n_tests = 20

        for i in range(n_tests):
            y0 = np.random.randint(0, 2, n)
            y1 = np.random.randint(0, 2, n)
            reindices = np.random.permutation(n)
            assert(accuracy(y0, y1) == accuracy(y0[reindices], y1[reindices]))

    def test_symetry(self):
        n = 10
        n_tests = 20

        for i in range(n_tests):
            y0 = np.random.randint(0, 2, n)
            y1 = np.random.randint(0, 2, n)
            assert(accuracy(y0, y1) == accuracy(y1, y0))


class HingeLossTest(unittest.TestCase):

    def _generator_labels(self, n):
        return np.random.randint(0, 2, n)*2-1

    def test_loss(self):
        n = 20
        y0 = np.random.random(n)*2-1
        y1 = self._generator_labels(n)

        thresholds = [0, 1, 2]
        for thr in thresholds:
            lossf = Hinge(thr)
            lossf.loss(y0, y1)

    def test_gradient(self):
        n, n_feats = 20, 10
        y0 = np.random.random(n)*2-1
        y1 = self._generator_labels(n)
        x = np.random.random((n, n_feats))

        thresholds = [0, 1, 2]
        for thr in thresholds:
            lossf = Hinge(thr)
            grad_w, grad_w0 = lossf.gradient_loss(y0, y1, x)
            assert(len(grad_w) == n_feats)

class SVMTest(unittest.TestCase):

    def _instantiator(self):
        loss=['Hinge', Hinge()]
        batch_size=[10]
        n_epochs=[0, 100]
        learning_rate=[0.0001, 1.]
        stop_step=[.000001, 100]
        lambda_par=[0.01, 1., 10.]
        verbose=[True, False]
        history=[True, False]
        possibilities = [loss, batch_size, n_epochs, learning_rate, stop_step,
                         lambda_par, verbose, history]
        for p in product(*possibilities):
            model = SVM(*p)
            yield p, model

    def test_initialization(self):
        n, n_feats = 100, 20
        data = np.random.random((n, n_feats))
        labels = np.random.randint(0, 2, n)*2-1

        for p, model in self._instantiator():
            ## General asserts
            assert(model.optimizer == 'SGD')
            assert(model.batch_size == p[1])
            assert(model.n_epochs == p[2])
            assert(model.stop_step == p[4])
            assert(model.lambda_par == p[5])
            assert(model.w is None)
            assert(model.w0 is None)

            ## Special cases
            if not p[7]:
                assert(model.train_loss_history is None)
                assert(model.test_loss_history is None)
                assert(model.train_accuracy_history is None)
                assert(model.test_accuracy_history is None)

            ## Weights initialization
            model._initialization_weights(n_feats, init_type='gauss')
            model._reset_model()
            model._initialization_weights(n_feats, init_type='zeros')
            model._reset_model()
            model._reset_history()

            ## Batch creation testing
            for x_batch, y_batch in model._batch_generator(data, labels):
                assert(len(x_batch) >= p[1])

            ## Computer functions
            if p[7]:
                model._initialization_weights(n_feats, init_type='gauss')
                model.compute_epoch_measures(data, labels, None, None)
                model.compute_epoch_measures(data, labels, data, labels)

    def test_fitmodel(self):
        n, n_feats = 100, 5
        data = np.random.random((n, n_feats))
        labels = np.random.randint(0, 2, n)*2-1

        for p, model in self._instantiator():
            model.n_epochs = 100
            model.fit(data, labels)
            model.fit(data, labels, data, labels)
            model.predict(data)
            model.score(data, labels)
            if p[7]:
                assert(model.epoch_learned == len(model.train_loss_history))
                assert(model.epoch_learned == len(model.train_accuracy_history))
                assert(model.epoch_learned == len(model.test_loss_history))
                assert(model.epoch_learned == len(model.test_accuracy_history))


if __name__ == '__main__':
    unittest.main()

