from my_model import square

import pytest

@pytest.mark.parametrize(
	'inputs',[
	2,3,4,6.2]
	)


def test_square_give_correct_values(inputs):
	#When 
	subject = square(inputs)
	#Then
	assert isinstance(subject,int)	