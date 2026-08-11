import pandas as pd

class ConfidenceFilter:
    def __init__(self, threshold=0.75):
        self.threshold = threshold

    def apply_filter(self, df, prob_col='probability'):
        if prob_col not in df.columns:
            raise ValueError(f"Column '{prob_col}' not found in dataframe.")
        filtered_df = df.copy()
        filtered_df['status'] = filtered_df[prob_col].apply(
            lambda x: 'Accepted' if x >= self.threshold else 'Manual Review Required'
        )
        return filtered_df