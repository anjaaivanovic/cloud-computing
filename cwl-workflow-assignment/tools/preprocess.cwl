cwlVersion: v1.2
class: CommandLineTool

requirements:
    DockerRequirement:
        dockerPull: anjaaivanovic/cwl-tools
    
baseCommand:
    - python3
    - /app/scripts/preprocess.py

inputs:
    csv:
        type: File
        inputBinding:
            position: 1

outputs:
    processed_csv:
        type: File
        outputBinding:
            glob: processed.csv