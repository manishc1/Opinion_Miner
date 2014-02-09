#! /bin/sh

#echo "Are you sure to initiate learning [Y/N] : \c"
#read answer
#yes="Y"
#echo $answer $yes
#if ["$answer" -eq "$yes"]
#then
	/usr/bin/python "trainWrapper.py" $1  > /dev/null 2>&1
	./svm_light/svm_learn data/trainAttributeVector.data data/model > /dev/null 2>&1
#fi
