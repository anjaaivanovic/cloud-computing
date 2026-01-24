cwlVersion: v1.2
class: CommandLineTool

requirements:
    DockerRequirement:
        dockerPull: anjaaivanovic/cwl-tools

baseCommand:
    - python3
    - /app/scripts/create_folds.py

inputs:
    k:
        type: int
        inputBinding:
            position: 1

outputs:
    folds:
        type: int[]
        outputBinding:
            glob: folds.json
            loadContents: true
            outputEval: $(JSON.parse(self[0].contents))