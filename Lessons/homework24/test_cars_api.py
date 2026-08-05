import pytest

from logger_config import logger

BASE_URL = "http://127.0.0.1:8080"


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 3),
        ("brand", 10),
        ("engine_volume", 7),
        ("price", 15),
        ("year", 20),
        ("brand", 25),
    ]
)
class TestCarsSearch:

    def test_search_cars(self, session, sort_by, limit):

        logger.info(
            f"Search cars: sort_by={sort_by}, limit={limit}"
        )

        response = session.get(
            f"{BASE_URL}/cars",
            params={
                "sort_by": sort_by,
                "limit": limit
            }
        )

        logger.info(f"Status code: {response.status_code}")

        assert response.status_code == 200

        cars = response.json()

        logger.info(f"Returned {len(cars)} cars")

        assert len(cars) <= limit

        if sort_by == "price":
            prices = [car["price"] for car in cars]
            assert prices == sorted(prices)

        elif sort_by == "year":
            years = [car["year"] for car in cars]
            assert years == sorted(years)

        elif sort_by == "brand":
            brands = [car["brand"] for car in cars]
            assert brands == sorted(brands)

        elif sort_by == "engine_volume":
            engines = [car["engine_volume"] for car in cars]
            assert engines == sorted(engines)

        logger.info("Test PASSED\n")