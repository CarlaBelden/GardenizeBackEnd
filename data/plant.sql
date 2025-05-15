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
(241, 'Ladybells', 'https://perenual.com/storage/species_image/541_adenophora_amethyst/thumbnail/2448px-Adenophora_cf._aurita_282098345350529.jpg', 'Average', 'Full Sun', 3, 8, 'Amethyst blue Flowers', 'Spring', FALSE, 'Ladybells (Adenophora ''Amethyst'') is a stunning perennial plant with eye-catching purple blooms. This showy, low maintenance, and drought tolerant variety of ladybells is the perfect addition to any landscape. Its tall, spire-like stems and bell-shaped flowers provide an attractive display of color and texture, making it the focal point of any garden. Ladybells bloom in summer, producing blooms that are not only delicate in appearance but also fragrant, attracting plenty of pollinators throughout the season. It is also great for cut flowers, bringing elegance to any bouquet. With it''s easy care, long blooming period and attractive look, Ladybells (Adenophora ''Amethyst'') is an amazing plant for the garden.'),
(5497, 'Sweet Basil', 'https://perenual.com/storage/species_image/5497_ocimum_basilicum/thumbnail/40248200770_b483e688a0_b.jpg', 'Frequent', 'Full Sun', 2, 11, 'Yes', 'Summer', TRUE, 'Sweet Basil (Ocimum basilicum) is a delicious leafy herb commonly used in cooking. It grows best in warm, humid climates and can be propagated with seeds or cuttings. Its slim green leaves have a bright and spicy flavor with hints of anise and lemon, making it a wonderful addition to salads, pastas, tomatoes, and more. Sweet Basil is a great source of vitamin A, vitamin C, vitamin K, and iron. It is an easy-to-grow herb that adds a unique flavor and an extra nutrient boost to any dish!'),
(728, 'Aloe Vera', 'https://perenual.com/storage/species_image/728_aloe_vera/thumbnail/52619084582_6ebcfe6a74_b.jpg', 'Low', 'Bright Indirect Light', 10, 12, 'Yes', NULL, TRUE, 'Aloe vera is a fantastic plant species known for its many amazing health benefits. Consisting of thick leaves with a gel-like interior, aloe vera has long been used as a traditional remedy for treating skin conditions. It is a great source of vitamins, minerals, and amino acids, making it a great natural remedy for common ailments. Aloe vera is also incredibly versatile, with the gel and sap being used for everything from digestive disorders to eye health. It is even believed to reduce inflammation and improve circulation. With its myriad of benefits, aloe vera is definitely an amazing plant species.'),
(4706, 'English lavender', 'https://perenual.com/storage/species_image/4706_lavandula_angustifolia_kerlavangem_sweet_romance/thumbnail/31305743805_4a11cf7184_b.jpg', 'Low to Moderate', 'Full Sun', 5, 8, 'Yes', 'Summer', FALSE, 'English lavender (Lavandula angustifolia ''KERLAVANGEM'' SWEET ROMANCE) is a sweet-scented, aromatic herb. Growing up to 2 feet in height, it features soft woody-green foliage and long stems that produce bluish-purple flowers during the mid-summer. This variety of lavender is resistant to extreme cold temperatures and can bloom continuously throughout the season. Its fragrant blooms provide an excellent source of nectar for birds and bees. Additionally, English lavender is well suited for potting and can be used in a variety of ways: the flowers make a great addition to floral arrangements; dried, they can be used to make essential oils, soaps, and fragrance sachets; they can also be used in baking, infusions, and teas.'),
(7168, 'Snake Plant', 'https://perenual.com/storage/species_image/7168_sansevieria_patens/thumbnail/27993887095_7bf4b9fe71_b.jpg', 'Low', 'Low to Bright Indirect Light', 10, 12, 'No', NULL, TRUE, 'Snake Plant is a species belonging to the Sansevieria genus. This distinctively attractive and resilient plant is native to regions of Japan and Africa. It features rigid, upright leaves that are deep green and marbled with silver-gray bands. Snake Plant is an extremely hardy plant that needs little attention and thrives in low light and dry conditions. It is known for its air-purifying qualities and is known to reduce VOCs, toxins, and pollen particles. Its long, firm leaves hold their shape even in environments of extreme temperature fluctuations or over-fertilized soil. With its versatility and ability to withstand neglect, it’s a great houseplant for busy households.'),
(5025, 'Tomato', 'https://perenual.com/storage/species_image/5025_lycopersicon_esculentum_rapunzel/thumbnail/pexels-photo-6314416.jpg', 'Average', 'Full Sun', 10, 11, 'Yes', 'Summer', FALSE, 'Tomato (Lycopersicon esculentum ''Rapunzel'') is an heirloom variety of tomato, popularly grown in Germany for centuries. Its large fruits are bright yellow, slightly elongated, and with thick walls. The taste is sweet and slightly tart, making it great for salads, canning, and sauces. Its strong vines can reach heights of up to 12 feet, and it is prolific producer with fruits that can weigh up to one pound. It is a very adaptable variety, accepting most soil and climate conditions without problems. It is both early season and indeterminate, so expect to have plenty of tomatoes on hand once they start bearing!'),
(9118, 'Hybrid Milkweed', 'https://perenual.com/storage/species_image/9118_asclepias_speciosa_x/thumbnail/15517847764_bbc386997a_b.jpg', 'Moderate', 'Full Sun', 3, 9, 'Yes', 'Summer', FALSE, 'Hybrid Milkweed (Asclepias speciosa x) is a species of milkweed with a unique hybrid blend of Asclepias speciosa and another milkweed species. This hardy plant features bright green oval leaves, clusters of spectacularly fragrant, deep pink flowers and attractive seed pods. It is a striking addition to any garden, and is an important source of food and shelter for butterfly and moth species. This species is drought tolerant and grows in well-drained, sunny areas. Drought-tolerant and low-maintenance, Hybrid Milkweed is a great addition to outdoor spaces and attract pollinators year-round.');


INSERT INTO project (
    project_name, posted_date, summary
) VALUES
('Kitchen Herb Garden', '2024-03-15', 'Growing fresh herbs indoors.'),
('Succulent Rescue', '2024-04-10', 'Reviving my neglected Aloe.'),
('Air-Purifying Indoor Setup', '2024-04-22', 'Trying snake plants for clean air.'),
('Edible Garden', '2024-05-01', 'Grow your own fruits, vegetables, and herbs. Includes raised beds, fruit trees, and berry bushes.'),
('Flower Garden', '2024-05-05', 'Create a vibrant flower display with various colors, textures, and pollinator-friendly designs.'),
('Butterfly Garden', '2024-05-10', 'Plant nectar-rich flowers and host plants to attract and support butterflies.');


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
