# Copyright 2025 Anonymous Authors. All rights reserved.
# Licensed under the MIT License, Version 1.0 (the "License");

"""
Action Model Module

This module contains the flow-matching action prediction head and related components.
The FlowmatchingActionHead is used to predict continuous actions from vision-language embeddings.
"""

from .ActionHeader import FlowmatchingActionHead

__all__ = ["FlowmatchingActionHead"]

