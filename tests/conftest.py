import os
import pytest

@pytest.fixture(scope="session")
def ajmc_en_sample_path():
    # super quick & dirty hard-coded variable
    return os.path.join(
        "/Users/matteo/Documents/AjaxMultiCommentary/HIPE2022-corpus/data/release/v0.1/",
        "HIPE-2022-ajmc-v0.1-sample-en.tsv"
    )


@pytest.fixture(scope="session")
def ajmc_de_sample_path():
    # super quick & dirty hard-coded variable
    return os.path.join(
        "/Users/matteo/Documents/AjaxMultiCommentary/HIPE2022-corpus/data/release/v0.1/",
        "HIPE-2022-ajmc-v0.1-sample-de.tsv"
    )