from .data_loss import LpLoss, VectorNormLoss, L1Loss, MSELoss, get_loss_fn, LOSSES_CLASSES as DATA_LOSSES

LOSSES_CLASSES = {**DATA_LOSSES}

__all__ = ["LpLoss",
            "VectorNormLoss",
            "L1Loss",
            "MSELoss"
        ]