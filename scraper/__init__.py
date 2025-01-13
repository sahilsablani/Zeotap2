from .segment_scraper import fetch_segment_docs
from .mparticle_scraper import fetch_mparticle_docs
from .lytics_scraper import fetch_lytics_docs
from .zeotap_scraper import fetch_zeotap_docs

__all__ = [
    "fetch_segment_docs",
    "fetch_mparticle_docs",
    "fetch_lytics_docs",
    "fetch_zeotap_docs",
]
