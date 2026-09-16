<h1 align="center">RMBench: Memory-Dependent Manipulation Benchmark</h1>

RMBench: Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design. <i>Under Review</i>, [Website](https://rmbench-anonymous.github.io/)

> Anonymous Authors — identity withheld for double-blind review.
>
> This is an anonymized repository released solely for peer review. Links that could reveal author identity (paper PDF, arXiv, model hubs, community pages) have been removed and will be restored upon acceptance.

# 📰 Updates

**2026.07.14** — Since the previously trained Mem-0 checkpoints were not backed up before our development machine was recycled, we have re-organized the training and now publicly release the retrained model weights:

- **M(1) tasks**: due to limited computational resources, all M1 tasks were trained jointly into a single multi-task `m1_mix` model. The complete model, the processed `m1_mix` dataset, training/inference configs, and all evaluation logs and videos are publicly released (Hugging Face links removed for double-blind review; they will be restored upon acceptance).
- **M(n) tasks**: per-task execution-module checkpoints for `battery_try`, `blocks_ranking_try`, `cover_blocks` and `press_button`, together with per-task normalization stats and evaluation results, are also released (links removed for double-blind review).

Detailed evaluation results can be found in the released model cards (links withheld during review).

# 🧑🏻‍💻 RMBench Usage

> This project is built upon [RoboTwin 2.0](https://github.com/robotwin-Platform/RoboTwin), and you can seamlessly transfer your policy code between the two projects.

## 1. Installation
First, prepare a conda environment.

```
conda create -n RMBench python=3.10 -y
conda activate RMBench
```

RMBench Repo: https://github.com/rmbench-anonymous/RMBench-Anonymous

```
git clone https://github.com/rmbench-anonymous/RMBench-Anonymous.git
```

Then, run `script/_install.sh` to install basic conda envs and CuRobo:

```
bash script/_install.sh
```

## 2. Download Assets
To download the assets, run the following command. If you encounter any rate-limit issues, please log in to your Hugging Face account by running `huggingface-cli login`:

```
bash script/_download_assets.sh
```

## 3. Download Data

Please run the following command to download all data.

```
bash script/_download_data.sh
```

<details>
<summary>If you need to collect the data (we actually recommend downloading it directly)</summary>

> In RMBench, we always use `demo_clean` setting.

Running the following command will first search for a random seed for the target collection quantity, and then replay the seed to collect data.

Please strictly follow our tutorial in [RoboTwin 2.0 Doc - Collect Data](https://robotwin-platform.github.io/doc/usage/collect-data.html).

```
bash collect_data.sh ${task_name} ${task_config} ${gpu_id}
# Example: bash collect_data.sh cover_blocks demo_clean 0
```
</details>

## 4. Run Policies

1. Mem-0 (ours): [See Mem-0 Document](./policy/Mem-0/README.md)
2. DP: [See DP Document](https://robotwin-platform.github.io/doc/usage/DP.html)
3. ACT: [See ACT Document](https://robotwin-platform.github.io/doc/usage/ACT.html)
4. Pi 0.5: [See Pi 0.5 Document](https://robotwin-platform.github.io/doc/usage/Pi05.html)
5. X-VLA: [See X-VLA Document](./policy/X-VLA/README.md)
6. Other Policies (Pi0, RDT, etc): [See Document](https://robotwin-platform.github.io/doc/usage) and [See Folder](./policy/)
6. **Configure your policy:** [See Tutorial Here](https://robotwin-platform.github.io/doc/usage/deploy-your-policy.html)

# 👍 Citations

Citation information is withheld for double-blind review and will be provided upon acceptance.

# 🏷️ License

This repository is released under the MIT license. See [LICENSE](./LICENSE) for additional details.
