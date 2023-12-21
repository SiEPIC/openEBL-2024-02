
# openEBL Design Submissions

- The Canadian Silicon Photonics Foundry, <a href="https://siepic.ca/fabrication/">SiEPICfab</a>, presents the open electron beam lithography (EBL) fabrication process, where former and current students of <a href="https://siepic.ca/education/">SiEPIC</a> workshops and courses can submit their design for manufacturing and testing.
- More details about <a href="https://siepic.ca/openEBL/">openEBL</a>.
- Slides: <a href="https://docs.google.com/presentation/d/18B8UAUWxal7vW1-bIIp5o7Mb6nLZ9Ep64zdLF2bcjPQ">link</a>

# Submission instructions:

The submission involves several steps. First, you need to create your design(s) using the process design kit (PDK) for this specific fabrication run. Then you need to create a Fork of this repository, commit your design(s), ensure that it passes the checks, and create a pull request. Once your pull request is approved, your design(s) will be merged into the layout for fabrication. You should verify that your design is correctly merged. Once the designs are fabricated, they will be tested, and the measurement results will be posted in this repository.

## Design software and PDK installation instructions:
 - Design tools and process design kit (SiEPIC-EBeam-PDK, KLayout implementation)<a href="https://github.com/siepic/SiEPIC_EBeam_PDK/wiki/Installation-instructions">installation instructions</a>. 

## Submission via GitHub
 
 - Create an account on GitHub
 - Fork a copy of this GitHub repository into your own account:  <a href="https://github.com/SiEPIC/openEBL-2024-02/fork">Create a new fork</a> 
 - [Optional] Install GitHub Desktop (or git) on your computer, and Clone a local copy: <a href="x-github-client://openRepo/https://github.com/SiEPIC/openEBL-2024-02">Open with GitHub Desktop</a>
 - Upload your design(s) into the "submissions" folder, as a binary file, namely a .gds (GDSII format) or .oas (OASIS format) file. The filename must contain your <a href="https://www.edx.org/learn/engineering/university-of-british-columbia-silicon-photonics-design-fabrication-and-data-ana">edX.org</a> username, e.g., EBeam_LukasChrostowski_rings.oas
    - This can be done via the GitHub web page, by navigating to the <a href=blob/main/submissions>submissions folder</a>, then clicking on Add file, and Upload files. 
    - Click Commit changes, and wait for the verification to complete
    - If there are errors, please review and correct the errors
 - Alternatively upload your Python file, which will be compiled by a GitHub Action.  
   - For KLayout designs, use the "submissions/KLayout Python" folder, namely a .py (Python format) file.  e.g., EBeam_LukasChrostowski_MZI.py.  The Python file should save a gds or oas file into the parent "submissions" folder. The Python script needs to be executable in non-GUI mode, namely using "import klayout SiEPIC SiEPIC-EBeam-PDK"
 - Create a <a href="https://help.github.com/articles/using-pull-requests/">Pull Request</a> -- this will notify the team of your contribution, which we can aggregate into the main design file
 - Return to the main repository, and check for the merged design

## Automated GitHub Actions

1) Running the files in the "submissions/KLayout Python" folder, to generate the designs
2) Performing Manufacturing DRC verification on the designs in the "submissions" folder, and outputing the errors as an Artifact
3) Performing Functional verification on the designs in the "submissions" folder, and outputing the errors as an Artifact
4) Merging the designs from the "submissions" folder, and outputing merged layout as an Artifact

## Latest Merge Script Files

<!-- start-link -->
https://github.com/SiEPIC/openEBL-2024-02/actions/runs/7282274159/artifacts/1127841211
<!-- end-link -->
