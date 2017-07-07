FROM kaggle/python:latest

RUN mkdir /working
RUN mkdir /working/data
ADD features.txt /working/data/features.txt
ADD target.txt /working/data/target.txt
ADD svm.py /working/svm.py
ADD tests.py working/tests.py
ADD Report-ToyProblem.ipynb /working/Report-ToyProblem.ipynb
#ADD requirements.txt /working/requirements.txt

WORKDIR /working
#RUN apt-get update && apt-get upgrade
#RUN pip3 install -r requirements.txt

ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

EXPOSE 8888
CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0"]
