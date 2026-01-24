cwlVersion: v1.2
class: Workflow

inputs:
    csv_file: File
    column_name: string
    training_set_percentage: float


steps:
    preprocess:
        run: tools/preprocess.cwl
        in:
            csv: csv_file
        out: [ processed_csv ]
    train:
        run: tools/train.cwl
        in:
            csv_file: preprocess/processed_csv
            column_name: column_name
            training_set_percentage: training_set_percentage
        out: [ metrics ]
outputs:
    result:
        type: File
        outputSource: train/metrics
