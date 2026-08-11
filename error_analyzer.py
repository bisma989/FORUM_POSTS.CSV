import pandas as pd

class ErrorAnalyzer:
    def __init__(self, df, true_col='true_label', pred_col='pred_label', text_col='text', prob_col='probability'):
        self.df = df
        self.true_col = true_col
        self.pred_col = pred_col
        self.text_col = text_col
        self.prob_col = prob_col

    def identify_false_positives(self):
        fp_cases = self.df[(self.df[self.true_col] == 0) & (self.df[self.pred_col] == 1)]
        fn_cases = self.df[(self.df[self.true_col] == 1) & (self.df[self.pred_col] == 0)]
        return pd.concat([fp_cases, fn_cases])

    def identify_sarcasm(self, sarcasm_keywords=None):
        if sarcasm_keywords is None:
            sarcasm_keywords = ['yeah right', 'great, just great', 'oh sure', 'love how', 'so wonderful', 'totally']
        pattern = '|'.join(sarcasm_keywords)
        return self.df[self.df[self.text_col].str.contains(pattern, case=False, na=False)]

    def identify_ambiguous(self, lower_bound=0.40, upper_bound=0.60):
        if self.prob_col in self.df.columns:
            return self.df[(self.df[self.prob_col] >= lower_bound) & (self.df[self.prob_col] <= upper_bound)]
        return pd.DataFrame()