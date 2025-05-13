-- read into psql with:
-- \i data/plant.sql
DROP TABLE IF EXISTS plant_project;
DROP TABLE IF EXISTS comment;
DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS plant;


CREATE TABLE plant (
    plant_id INTEGER PRIMARY KEY,
    common_name VARCHAR(255) NOT NULL,
    default_image VARCHAR(1024),
    watering VARCHAR(255) NOT NULL,
    sunlight  VARCHAR(255) NOT NULL,
    hardiness_min INTEGER NOT NULL,
    hardiness_max INTEGER NOT NULL,
    flowers VARCHAR(255),
    flowering_season  VARCHAR(255),
    indoor Boolean,
    description TEXT NOT NULL
);

CREATE TABLE project (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    posted_date DATE NOT NULL DEFAULT NOW(),
    summary TEXT NOT NULL
);

CREATE TABLE comment (
    comment_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES project(project_id) ON DELETE CASCADE,
    plant_id INTEGER REFERENCES plant(plant_id),
    posted_date DATE NOT NULL DEFAULT NOW(),
    comment TEXT
);

CREATE TABLE plant_project (
    plant_project_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES project(project_id) ON DELETE CASCADE,
    plant_id INTEGER REFERENCES plant(plant_id)
);



INSERT INTO plant (
    plant_id, common_name, default_image, watering, sunlight,
    hardiness_min, hardiness_max, flowers, flowering_season, indoor, description
) VALUES
(47, 'Butterfly Variegated Japanese Maple', 'https://perenual.com/storage/species_image/47_acer_palmatum_butterfly/thumbnail/20251027248_dc9cfd6f65_b.jpg', 'Average', 'Full Sun', 6, 6, 'Reddish-Purple Flowers', 'Spring', FALSE, 'Acer palmatum ''Butterfly'' is a stunning variegated Japanese maple with bright yellow foliage that''s sure to draw attention. Its fine-textured leaves feature a network of veins in shades of green and white, resembling the pattern on a butterfly''s wings. In the summer, the foliage fades to a pale cream color, and in the autumn, the yellow-green edges flush pink. Its weeping form creates an enchanting, cascading display. This low-maintenance plant tolerates a variety of soils and is drought-tolerant once established, making it a wonderful choice for gardens of all sizes. Its stunning leaf display makes Butterfly Variegated Japanese Maple a must-have feature for the garden.'),
(216, 'Appalachian Red Redbud', 'https://perenual.com/storage/species_image/216_cercis_canadensis_appalachian_red/thumbnail/Cercis_canadensis_Appalachian_Red_1zz.jpg', 'Average', 'Full Sun', 5, 5, 'Pink Flowers ', 'Spring', FALSE, 'The Appalachian Red Redbud is a beautiful medium-sized deciduous tree native to the United States. Its stunning deep red blooms make it a stunning addition to any garden, and it is a favorite for those who are looking for something special. The large, heart-shaped leaves turn an amazing yellow-orange in autumn, adding another layer of beauty to this unique plant. It''s also very easy to care for, making it a great addition for those who don''t have a lot of experience with gardening. In addition, the Appalachian Red Redbud is also a symbol of hope and renewal, making it a meaningful plant to have in your home.'),
(250, 'Red Flowering Dogwood', 'https://perenual.com/storage/species_image/250_cornus_florida_var_rubra/thumbnail/10108500273_70c8821e33_b.jpg', 'Average', 'Full Sun', 6, 6, 'White (bracts) Flowers', 'Spring', FALSE, 'The Red Flowering Dogwood (Cornus florida ''var. rubra'') is a truly amazing plant species. With vivid, deep red blossoms from late spring to early summer, the Red Flowering Dogwood adds beautiful color to any landscape. Its broad, spreading branches are equally stunning, with auburn-toned bark providing year-round interest. This plant is also drought tolerant, making it a great choice for both shade and sun in warmer climates. The vibrant flowers not only attract birds and other pollinators, but they also make lovely cut flowers as well. Truly, the Red Flowering Dogwood is a standout species.'),
(241, 'Ladybells', 'https://perenual.com/storage/species_image/541_adenophora_amethyst/thumbnail/2448px-Adenophora_cf._aurita_282098345350529.jpg', 'Average', 'Full Sun', 3, 8, 'Amethyst blue Flowers', 'Spring', FALSE, 'Ladybells (Adenophora ''Amethyst'') is a stunning perennial plant with eye-catching purple blooms. This showy, low maintenance, and drought tolerant variety of ladybells is the perfect addition to any landscape. Its tall, spire-like stems and bell-shaped flowers provide an attractive display of color and texture, making it the focal point of any garden. Ladybells bloom in summer, producing blooms that are not only delicate in appearance but also fragrant, attracting plenty of pollinators throughout the season. It is also great for cut flowers, bringing elegance to any bouquet. With it''s easy care, long blooming period and attractive look, Ladybells (Adenophora ''Amethyst'') is an amazing plant for the garden.');


INSERT INTO project (
    project_name, posted_date, summary
) VALUES
('Kitchen Herb Garden', '2024-03-15', 'Growing fresh herbs indoors.'),
('Succulent Rescue', '2024-04-10', 'Reviving my neglected Aloe.'),
('Air-Purifying Indoor Setup', '2024-04-22', 'Trying snake plants for clean air.');


INSERT INTO comment (
    project_id, plant_id, posted_date, comment
) VALUES
(1, 216, '2024-03-16', 'Possible front yard show stopper.'),
(2, 47, '2024-04-11', 'Great idea for the back yard'),
(3, 250, '2024-04-23', 'Something to consider is foliage.'),
(1, 216, '2024-03-17', 'Great for spring foliage.');

INSERT INTO plant_project (
    plant_project_id, project_id, plant_id
) VALUES
(1, 2, 216),
(2, 3, 47),
(3, 1, 250),
(4, 3, 216);
