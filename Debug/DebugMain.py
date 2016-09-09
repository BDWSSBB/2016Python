from DebugInherit import MyCat
from DebugBase import MyPet

class MainClass:
    def main():
        cat_1 = MyCat("Rexasaur")
        cat_2 = MyCat("Smith")
        cat_1.meow()
        cat_1.get_cats_age()
        my_dog_fido = MyPet("Fido")
        my_dog_fido.pet()
        my_dog_fido.bark()
    if __name__ == "__main__":
        main()