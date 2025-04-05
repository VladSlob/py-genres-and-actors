   import init_django_orm  # noqa: F401
   from django.db.models import QuerySet
   from db.models import Genre, Actor

   def main() -> QuerySet:
       # Create genres
       genres = [
           ("Western",),
           ("Action",),
           ("Dramma",)
       ]
       for name in genres:
           Genre.objects.get_or_create(name=name[0])

       # Create actors
       actors = [
           ("George", "Klooney"),
           ("Kianu", "Reaves"),
           ("Scarlett", "Keegan"),
           ("Will", "Smith"),
           ("Jaden", "Smith"),
           ("Scarlett", "Johansson")
       ]
       for first_name, last_name in actors:
           Actor.objects.get_or_create(first_name=first_name, last_name=last_name)

       # Update genres and actors
       Genre.objects.filter(name="Dramma").update(name="Drama")
       Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
       Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

       # Delete genre and actors
       Genre.objects.filter(name="Action").delete()
       Actor.objects.filter(first_name="Scarlett").delete()

       # Return remaining actors
       return Actor.objects.filter(last_name="Smith")
