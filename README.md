# Continuous Benchmarking with CIGR and ASV

## Minimal example

1) `asv quickstart`, choose "benchmark suite in same repository"
2) set project name, url, branches, dependencies etc in `asv.conv.json`
3) If the main repo is not hosted on gitlab, import it there as "CI/CD for external repo"
    - you will requrie a personal access token for github
4) Create a read/write deploy key on the main repo, add the secret key as a file variable on the CIGR mirror
5) create a `.gitlab-ci.yml` as you would for any CIGR with a benchmarking job
    - the job's docker image must contain python as well as git
