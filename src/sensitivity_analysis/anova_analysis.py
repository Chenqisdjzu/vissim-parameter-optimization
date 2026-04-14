import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

class ANOVASensitivityAnalysis:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def run_anova(self, dependent_var: str, independent_vars: list):
        
        independent_formula = ' + '.join(independent_vars)
        formula = f'{dependent_var} ~ {independent_formula}'
        model = ols(formula, data=self.data).fit()
        anova_results = anova_lm(model)
        return anova_results

    def interpret_results(self, anova_results: pd.DataFrame):
        # Interpret ANOVA results here
        return anova_results

# Example usage:
# data = pd.read_csv('your_data.csv')
# anova_analysis = ANOVASensitivityAnalysis(data)
# results = anova_analysis.run_anova('dependent_variable', ['independent_var1', 'independent_var2'])
# print(results)