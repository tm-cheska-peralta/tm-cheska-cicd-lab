# CI/CD Lab
Lab instructions can be found [here](https://docs.google.com/presentation/d/1Kj12YCa7hGpqr6Pzaoq4MADLdRo2Elie8S6H0wNx89U/edit#slide=id.g2f081185786_0_160).

## Repository Files
- **src**
   - `main.py`
     - A simple python script that accepts number parameters `num_a` and `num_b`, prints each value, then prints the sum.
- **.github/workflows**
  - `python-template.yml`
    - Template that contains two jobs:
      1. **run_python_code**: Runs the python file `main.py` from the `src` folder with env vars `NUM_A` and `NUM_B` as input.
      2. **print_secret**: Echos the value of the `SECRET` env variable with space in between.
  - `env_1.yml`
    - Workflow that uses the `python-template.yml` using the environment: **tm-cicd-lab-env-1**
  - `env_2.yml`
    - Workflow that uses the `python-template.yml` using the environment: **tm-cicd-lab-env-2**
   
## Workflow Runs
Workflow runs viewable [here](https://github.com/tm-cheska-peralta/tm-cheska-cicd-lab/actions).
