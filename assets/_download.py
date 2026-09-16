from huggingface_hub import snapshot_download

# NOTE: The dataset repository id has been anonymized for double-blind review.
# The original download link will be restored upon acceptance.
snapshot_download(
    repo_id="anonymized-for-review/RMBench",
    allow_patterns=["embodiments/**", "objects/**"],
    local_dir=".",
    repo_type="dataset",
    resume_download=True,
)
