import pytest
from os.path import join

import mminte

class TestInteractions:

    def test_growth_rates(self, data_folder):
        model_files = ['BT.sbml', 'FP.sbml']
        source_models = [ join(data_folder, x) for x in model_files ]
        pair_models = mminte.create_interaction_models(source_models, output_folder=data_folder)
        assert len(pair_models) == 1
        assert pair_models[0] == '{0}/BTxFP.json'.format(data_folder)

        growth_rates = mminte.calculate_growth_rates(pair_models, join(data_folder, 'western.json'))
        assert growth_rates.at[0,'A_ID'] == 'BT'
        assert growth_rates.at[0,'B_ID'] == 'FP'
        assert growth_rates.at[0,'TYPE'] == 'Parasitism'
        assert growth_rates.at[0,'TOGETHER'] == pytest.approx(0.49507501)
        assert growth_rates.at[0,'A_TOGETHER'] == pytest.approx(0.27746256)
        assert growth_rates.at[0,'B_TOGETHER'] == pytest.approx(0.21761245)
        assert growth_rates.at[0,'A_ALONE'] == pytest.approx(0.44073842)
        assert growth_rates.at[0,'B_ALONE'] == pytest.approx(0.16933796)
        assert growth_rates.at[0,'A_CHANGE'] == pytest.approx(-0.37045977)
        assert growth_rates.at[0,'B_CHANGE'] == pytest.approx(0.28507777)

    def test_not_enough_source(self, data_folder):
        source_models = mminte.create_interaction_models([join(data_folder, 'BT.sbml')])
        assert len(source_models) == 0

    def test_bad_source_file(self, data_folder):
        model_files = ['BT.sbml', 'FP.sbml', 'BAD.sbml']
        source_models = [ join(data_folder, x) for x in model_files ]
        with pytest.raises(IOError):
            mminte.create_interaction_models(source_models, output_folder=data_folder)

    def test_bad_extension(self, data_folder):
        model_files = ['BT.sbml', 'FP.bad']
        source_models = [ join(data_folder, x) for x in model_files ]
        with pytest.raises(IOError):
            mminte.create_interaction_models(source_models, output_folder=data_folder)
