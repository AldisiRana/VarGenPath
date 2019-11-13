# -*- coding: utf-8 -*-

"""Tests for VarGenPath utils."""

import pandas as pd
import pytest

from vargenpath.utils import file_reader, get_associated_genes
from vargenpath.constants import VARIANT_LIST_PATH

@pytest.fixture
def variants():
    return file_reader(VARIANT_LIST_PATH)


def test_file_reader():
    content = variants()
    assert(type(content), list)
    assert(len(content), 27)


def test_get_associated_genes():
    content = variants
    test_df = get_associated_genes(content)
    assert(type(test_df), pd.DataFrame)
    assert(len(test_df.columns), 4)
    assert 'interaction' in test_df.columns
