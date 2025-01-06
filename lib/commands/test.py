import click
from pathlib import Path
from ..options import MyPath
from .utils import load_saved_options_cascade, setup_trainer

@click.command()
@click.argument("base_name")
@click.option("--save-images", is_flag=True)
def test(base_name, save_images):
    scale_factors = [8, 4, 2]
    result_dirs = [
        Path(MyPath.root_dir) / "results" / f"{base_name}-factor-{factor}"
        for factor in scale_factors
    ]
    
    trainer_options = [
        load_saved_options_cascade(MyPath.root_dir, base_name, factor=factor)
        for factor in scale_factors
    ]

    input_dir = Path(MyPath.root_dir) / "data" / "celeba" / "test" 
    output_base_dir = Path(MyPath.root_dir) / "results" / f"{base_name}-cascaded"
    
    with setup_trainer(trainer_options[0]) as trainer:
        trainer.test_cascaded(
            input_dir=input_dir,
            output_base_dir=output_base_dir,
            trainer_options=trainer_options,
            scale_factors=scale_factors,
            save_images=save_images,
        )
