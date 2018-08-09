from unittest import TestCase
from ..build import q04_correlation_plot
from greyatomlib.statlog_german_credit_data_project.q03_encode_features.build import q03_encode_features
from greyatomlib.statlog_german_credit_data_project.q01_load_data_and_add_column_names.build import q01_load_data_and_add_column_names
from inspect import getfullargspec

path = "data/GermanData.csv"
data=q01_load_data_and_add_column_names(path)
data=q03_encode_features(data)
q04_correlation_plot(data)


class Test_encode_features(TestCase):
    def test_args(self):
        arg = getfullargspec(q04_correlation_plot).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))
