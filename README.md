# Showdark Ticketing

This ticketing app was a group project designed to cement our understanding of how to connect backend (in this case Django) with frontend development (AngularJs). Contributing members were [Hannah Hall], [Sule Allen], [Jessica Wynn], and [Joe Kane].

#### To run the app:

In your terminal, navigate to the directory where you want to run the program from and type the following commands:
```sh
$ git clone https://github.com/nss-day-cohort-13/eventshine-showdark.git
```

Now, move into the `showdark` directory and run the following command to create the database tables:

```sh
$ python manage.py migrate
```

Next, open a new tab in your terminal and navigate to the `static` directory:
```sh
$ cd showdark/tickets/static
```

Showdark uses a few dependencies, so install them by typing:
```sh
$ npm install
$ bower install
$ gulp
```

That last `gulp` command start the Sass compiler, which is used for all the styling and layout. Finally, go back to the first `showdark` directory and run `python manage.py runserver` Point your web browser to `localhost:8080` and you're ready to use the app.

#### Under the hood:

The goal of this group project was to recreate a famous ticketing service as a means of learning how to develop a web app from start to finish, utilizing the MVC pattern. The models and their properties are as follows:

##### Events
- Name
- Description
- City
- Start date
- End date
- Venue (foreign key of Venue model)

##### Venue
- Name
- Address
- City
- State
- Zip Code
- Capacity
- Contact

##### UserEvent
- UserId (foreign key of User model)
- EventId (foreign key of Event model)

##### User
- Built-in Django [user authentication model](https://docs.djangoproject.com/en/1.10/topics/auth/default/#creating-users)

Once you sign in/register, you have the ability to view all, register for, and create as many events as you wish. Once the event capacity has been reached, no more users will be able to register for that event.


   [Hannah Hall]: <http://github.com/hannahhall>
   [Sule Allen]: <http://github.com/sulaiman-allen>
   [Jessica Wynn]: <http://github.com/Jessicashinjol>
   [Joe Kane]: <http://github.com/josephkane>
   [http-server]: <https://www.npmjs.com/package/httpserver>

