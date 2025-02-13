"""Visualization routines."""

import lazy_loader as lazy

__getattr__, __dir__, __all__ = lazy.attach(
    __name__,
    submodules=["backends", "_scraper", "ui_events"],
    submod_attrs={
        "backends._abstract": ["Figure3D"],
        "backends.renderer": [
            "set_3d_backend",
            "get_3d_backend",
            "use_3d_backend",
            "set_3d_view",
            "set_3d_title",
            "create_3d_figure",
            "close_3d_figure",
            "close_all_3d_figures",
            "get_brain_class",
        ],
        "circle": ["circular_layout", "plot_channel_labels_circle"],
        "epochs": [
            "plot_drop_log",
            "plot_epochs",
            "plot_epochs_psd",
            "plot_epochs_image",
        ],
        "evoked": [
            "plot_evoked",
            "plot_evoked_image",
            "plot_evoked_white",
            "plot_snr_estimate",
            "plot_evoked_topo",
            "plot_evoked_joint",
            "plot_compare_evokeds",
        ],
        "ica": [
            "plot_ica_scores",
            "plot_ica_sources",
            "plot_ica_overlay",
            "_plot_sources",
            "plot_ica_properties",
        ],
        "misc": [
            "plot_cov",
            "plot_csd",
            "plot_bem",
            "plot_events",
            "plot_source_spectrogram",
            "_get_presser",
            "plot_dipole_amplitudes",
            "plot_ideal_filter",
            "plot_filter",
            "adjust_axes",
            "plot_chpi_snr",
        ],
        "montage": ["plot_montage"],
        "raw": ["plot_raw", "plot_raw_psd", "plot_raw_psd_topo", "_RAW_CLIP_DEF"],
        "topo": ["plot_topo_image_epochs", "iter_topography"],
        "topomap": [
            "plot_evoked_topomap",
            "plot_projs_topomap",
            "plot_arrowmap",
            "plot_ica_components",
            "plot_tfr_topomap",
            "plot_topomap",
            "plot_epochs_psd_topomap",
            "plot_layout",
            "plot_bridged_electrodes",
            "plot_ch_adjacency",
            "plot_regression_weights",
        ],
        "utils": [
            "tight_layout",
            "mne_analyze_colormap",
            "compare_fiff",
            "ClickableImage",
            "add_background_image",
            "plot_sensors",
            "centers_to_edges",
            "concatenate_images",
            "_get_plot_ch_type",
        ],
        "_3d": [
            "plot_sparse_source_estimates",
            "plot_source_estimates",
            "plot_vector_source_estimates",
            "plot_evoked_field",
            "plot_dipole_locations",
            "snapshot_brain_montage",
            "plot_head_positions",
            "plot_alignment",
            "plot_brain_colorbar",
            "plot_volume_source_estimates",
            "link_brains",
            "set_3d_options",
        ],
        "_brain": ["Brain"],
        "_figure": [
            "get_browser_backend",
            "set_browser_backend",
            "use_browser_backend",
        ],
        "_proj": ["plot_projs_joint"],
    },
)
