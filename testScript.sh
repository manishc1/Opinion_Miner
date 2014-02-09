#! /bin/sh

/usr/bin/python "testWrapper.py" $1 0 10  > /dev/null 2>&1
./svm_light/svm_classify data/testAttributeVector.data data/model data/output > /dev/null 2>&1
