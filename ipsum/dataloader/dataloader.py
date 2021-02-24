import pandas as pd
import geopandas as gpd

from pathlib import Path


class DataLoader:
    """
    Loads input data.
    """

    def __init__(
        self,
        distance_matrix,
        region_shapefile,
        population_projection=None,
        services_shapefile=None,
    ):
        print("---> Loading data.")
        self.distance_matrix = self.load_distance_matrix(distance_matrix)
        self.region_shapefile = self.load_region_shapefile(region_shapefile)

        if population_projection:
            self.population_projection = self.load_population_projection(
                population_projection
            )
        if services_shapefile:
            self.services_shapefile = self.load_services_shapefile(services_shapefile)

    def load_distance_matrix(self, filename="distance-matrix.csv"):
        """
        Loads pre calculated Distance Matrix.
        :filename: string (default='distance-matrix.csv')
        :return: pd.Dataframe
        """
        filepath = Path(__file__).parent
        mod_path = "../../data/input/" + filename
        filepath = (filepath / mod_path).resolve()

        distance_matrix = pd.read_csv(filepath, dtype={"destination": str})

        if "geometry" in distance_matrix.columns:
            distance_matrix.drop(columns=["geometry"], inplace=True)

        distance_matrix["real_distance"] = distance_matrix["real_distance"].fillna(
            10000
        )

        return distance_matrix

    def load_population_projection(self, filename="population-projection.csv"):
        """
        (Optional) Load pre calculated population projection.
        Used to produce estimations on services provision to a future date.
        :filename: string
        :return: pd.DataFrame
        """

        population_projection = pd.read_csv(
            "../../data/input/" + filename, dtype={"Unnamed: 0": str}
        )
        population_projection.rename(columns={"Unnamed: 0": "BGRI"}, inplace=True)
        population_projection.index = population_projection["BGRI"]

        return population_projection

    def load_region_shapefile(self, filename="region-shapefile.shp"):
        """
        Load the shapefile with polygons for the desired region.
        For Portugal optimizations, should be something like
        gdf_freguesias_CAOP2018
        :filename: string
        :return: gpd.GeoDataFrame
        """

        filepath = Path(__file__).parent
        mod_path = "../../data/input/shapefile/" + filename
        filepath = (filepath / mod_path).resolve()

        region_shapefile = gpd.read_file(filepath)
        region_shapefile = region_shapefile[region_shapefile["DTMN11"] == "1107"]

        return region_shapefile

    def load_services_shapefile(self, filename="services-shapefile"):
        """
        (Optional) Load the shapefile with the pois or services to be
        distributed and optimized. If an hipotetical distribution is expected
        as result, disconsider this step.
        :filename: string
        :return: pd.DataFrame
        """
        services_shapefile = gpd.read_file("../../data/input/shapefile/" + filename)

        return services_shapefile
