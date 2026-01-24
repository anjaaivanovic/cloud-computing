cwlVersion: v1.2
class: CommandLineTool

requirements:
    DockerRequirement:
        dockerPull: anjaaivanovic/cwl-tools

baseCommand:
    - python3
    - /app/scripts/train.py

inputs:
    csv_file:
        type: File
        inputBinding:
            position: 1
    column_name:
        type: string
        inputBinding:
            position: 2
    training_set_percentage:
        type: float
        inputBinding:
            position: 3

outputs:
    metrics:
        type: File
        outputBinding:
            glob: metrics.txt