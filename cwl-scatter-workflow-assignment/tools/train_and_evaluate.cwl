cwlVersion: v1.2
class: CommandLineTool

requirements:
    DockerRequirement:
        dockerPull: anjaaivanovic/cwl-tools

baseCommand:
    - python3
    - /app/scripts/train_and_evaluate.py

inputs:
    csv_file:
        type: File
        inputBinding:
            position: 1
    column_name:
        type: string
        inputBinding:
            position: 2
    fold_id:
        type: int
        inputBinding:
            position: 3
    k:
        type: int
        inputBinding:
            position: 4

outputs:
    rmse:
        type: float
        outputBinding:
            glob: metrics.json
            loadContents: true
            outputEval: $(JSON.parse(self[0].contents)[0])
    prmse:
        type: float
        outputBinding:
            glob: metrics.json
            loadContents: true
            outputEval: $(JSON.parse(self[0].contents)[1])