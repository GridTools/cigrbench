# Continuous Benchmarking with CIGR and ASV

## Minimal example

1) `asv quickstart`, choose "benchmark suite in same repository"
2) set project name, url, branches, dependencies etc in `asv.conv.json`
3) If the main repo is not hosted on gitlab, import it there as "CI/CD for external repo"
    - you will requrie a personal access token for github to import
4) Set up CIGR infrastructure:
    - read/write deploy key from github to gitlab
    - read/write deploy key from gitlab to github
    - bors config
    - github action to push to the mirror on pushes to the benchmarked branches
4) Create a read/write deploy key on the main repo, add the secret key as a file variable on the CIGR mirror
5) create a `.gitlab-ci.yml` as you would for any CIGR with a benchmarking job and a publishing job
    - The benchmarking job will run on sarus on daint and can not push to github. It provides the results as an artifact.
    - The publishing job's docker image must contain python as well as git, it will push the history and update the github pages branch.
6) create the daint-node.json to specify the type of node you run on on daint.
