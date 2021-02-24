# from ipsum.dataloader.dataloader import DataLoader
from gurobi import *

import fire


def intro():
    """
    Display intro message
    :return: nothing
    """
    intro = """
        ___________   _____  _   _ __   ___
        |_   _| ___  /  ___  | | ||  \/  |
          | | |_/ /   `--.|  | | |  .  . |
          | |  __/   `--.  \ | | |  |\/| |
         _| |_| |    /\__/ / |_| |  |  | |
         \___/\_|    \____/ \___/ \_|  |_/

         A CLI application to optimize services
         distribuitions using justice principles.                        
                                 
    """
    print(intro)


def main(arg1, arg2, arg3=None, arg4=None):
    """
    Starts the execution with all possible outcomes.
    :param a: first argument
    :param b: second argument (default: 2)
    :return: pandas.Dataframe with distances to schools
    """
    try:
        from dataloader import DataLoader
    except (ModuleNotFoundError, RuntimeError):
        raise ModuleNotFoundError("Dataloder Module could not be loaded")
    intro()

    # data = DataLoader(
    #     "simplematrix-1107.csv", "gdf_BGRI_2011_CAOP2018_MACRO_Loures.shp"
    # )
    data = DataLoader(arg1, arg2, arg3, arg4)
    print(data.distance_matrix.head())


if __name__ == "__main__":

    fire.Fire({"main": main})
