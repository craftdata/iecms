## About
Mon Feb  5 14:42:20 2018
This is the first attempt at an Integrated Case Management System for Kenya. Agencies involved in this are:
1). Police
2). Director of Public Prosecutions
3). The Judiciary (Anchor)
4). Prisons
5) Citizens: Most importantly


This will track complaints trhough their life cycle through to concluded cases


## Development Method
There are an awful lot of tables (about 200) involved in this project. It would take more manpower than we have available to hand craft every single aspect of this system - so we have taken a code generation approach. (Look in the db section to see how we go about this)

The Idea is to completely round trip code, with no hand crafting of anything. Looked all over for a free/open source tool to to this, with no luck
So here is how I went about it:

1). Create an Entity Relationship Diagram (ERD) in pony at https://editor.ponyorm.com/user/nyimbi/IECMS/designer
To limit the effort required to do this - I am going to use mixins on the generated code to populate common fields on entities.
(Look at the mixin's in the db directory)

2). Take the ponyorm python generated and create a temporary model database (ctmp)

3). Since I intend to use flask-appbuilder, which has done quite a bit of framework heavy lifting, I need to convert the models to SQLalchemy models. To do that I used flask-sqlacodegen to reverse engineer the ctmp database

3). Theoretically I should now have a models.py file that I can use, but it does not have the mixins - so I take a somewhat elliptical approach and generate the views first. Using the codeg.py file. THEN

4). Modify the models.py file using fixup_models.py to add Mixins and manage the model at a meta-level

5). Hopefull now I have a skeleton that I can use, but that I still don't want to manage 


The code generation activity is ongoing, stay tuned.
# Development Environment
1). Editor Vim (Naturally)
2). Goodness, that seems to be all I am using!
