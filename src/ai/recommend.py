from src.schemas.category import CategoryForRecommend, CategoryIdWithRank
from src.schemas.recipe import RecipeForRecommend, RecipeWithRank
from src.schemas.recommend import IRecommend

class Recommend(IRecommend):
    def recommend_categories(self, psychorogical_test_results: list[str], categories: list[CategoryForRecommend], num_categories_to_recommend: int = 5) -> list[CategoryIdWithRank]:
        return super().recommend_categories(psychorogical_test_results, categories, num_categories_to_recommend)
    
    def recommend_recipes(self, contditions: list[str], recipes: list[RecipeForRecommend], num_recipes_to_recommend: int = 3) -> list[RecipeWithRank]:
        return super().recommend_recipes(contditions, recipes, num_recipes_to_recommend)