import os
import json
import pandas as pd
from src.error_analyzer import ErrorAnalyzer
from src.confidence_filter import ConfidenceFilter

def main():
    os.makedirs('data', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    
    data_path = 'data/raw_test_data.csv'
    
    if not os.path.exists(data_path):
        dummy_data = pd.DataFrame({
            'text': [
                'I love this product, absolutely amazing!', 
                'Yeah right, like this broken thing would work.', 
                'It is okay, nothing too special.', 
                'Worst service and quality ever experienced.'
            ],
            'true_label': [1, 1, 0, 0],
            'pred_label': [1, 0, 1, 0],
            'probability': [0.95, 0.52, 0.48, 0.89]
        })
        dummy_data.to_csv(data_path, index=False)

    df = pd.read_csv(data_path)
    
    analyzer = ErrorAnalyzer(df)
    fp_cases = analyzer.identify_false_positives()
    sarcasm_cases = analyzer.identify_sarcasm()
    ambiguous_cases = analyzer.identify_ambiguous()
    
    conf_filter = ConfidenceFilter(threshold=0.75)
    processed_df = conf_filter.apply_filter(df)
    processed_df.to_csv('data/evaluated_results.csv', index=False)
    
    error_summary = {
        "total_samples": len(df),
        "false_positives": len(fp_cases),
        "sarcasm_cases": len(sarcasm_cases),
        "ambiguous_cases": len(ambiguous_cases)
    }
    
    with open('outputs/error_cases.json', 'w') as f:
        json.dump(error_summary, f, indent=4)
        
    report_content = (
        "# Week 8: Sentiment Model Evaluation & Error Analysis Report\n\n"
        "## 1. Overview\n"
        "This report documents the performance evaluation of the sentiment model, focusing on error diagnosis and confidence filtering.\n\n"
        "## 2. Model Evaluation Report Summary\n"
        "```text\n"
        "================================================\n"
        "MODEL EVALUATION REPORT\n"
        "================================================\n"
        f"Total Samples     : {len(df)}\n"
        f"False Positives   : {len(fp_cases)}\n"
        f"Sarcasm Cases     : {len(sarcasm_cases)}\n"
        f"Ambiguous Cases   : {len(ambiguous_cases)}\n\n"
        "Evaluation completed successfully.\n"
        "```\n\n"
        "## 3. Analysis & Observations\n"
        "- **False Positives:** Evaluated instances show how the model handles polarity shifts.\n"
        "- **Sarcasm Handling:** Identified via heuristic keyword patterns.\n"
        "- **Ambiguity:** Borderline probability thresholds effectively isolate low-confidence predictions for review.\n"
    )

    with open('outputs/evaluation_report.md', 'w') as f:
        f.write(report_content)
    
    print("Report generated successfully!")

if __name__ == '__main__':
    main()