cwlVersion: v1.2
class: Workflow

requirements:
    ScatterFeatureRequirement: {}
    InlineJavascriptRequirement: {}

inputs:
    csv_file: File
    column_name: string
    k: int

steps:
    create_folds:
        run: ./tools/create_folds.cwl
        in:
            k: k
        out: [ folds ]
    
    preprocess:
        run: ./tools/preprocess.cwl
        in:
            csv_file: csv_file
        out: [ processed_csv_file ]

    train_and_evaluate:
        run: ./tools/train_and_evaluate.cwl
        in:
            csv_file: preprocess/processed_csv_file
            fold_id: create_folds/folds
            column_name: column_name
            k: k
        scatter: fold_id
        out: [ rmse, prmse ]

    write_metrics:
        run: ./tools/write_metrics.cwl
        in:
            rmse: train_and_evaluate/rmse
            prmse: train_and_evaluate/prmse
        out: [ metrics ]
    
outputs:
    metrics:
        type: File
        outputSource: write_metrics/metrics