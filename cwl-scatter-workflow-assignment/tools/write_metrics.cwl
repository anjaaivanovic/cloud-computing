cwlVersion: v1.2
class: CommandLineTool

requirements:
    DockerRequirement:
        dockerPull: anjaaivanovic/cwl-tools

baseCommand:
    - python3
    - /app/scripts/write_metrics.py

inputs:
    rmse:
        type: float[]
        inputBinding:
            prefix: --rmse
            separate: true

    prmse:
        type: float[]
        inputBinding:
            prefix: --prmse
            separate: true

outputs:
    metrics:
        type: File
        outputBinding:
            glob: metrics.json