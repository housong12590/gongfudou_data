from db.db_helper import SQLHelper

movies = """
    CREATE TABLE IF NOT EXISTS movies(
      id INT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(255) NOT NULL UNIQUE ,
      rating FLOAT DEFAULT 0 COMMENT '评分',
      type VARCHAR(50) COMMENT '类型 如2D 3D',
      cover VARCHAR(255) COMMENT '封面',
      box_office INT(11) DEFAULT 0 COMMENT '票房',
      length VARCHAR(10) COMMENT '时长',
      be_on BOOL DEFAULT TRUE COMMENT '是否上映',
      be_on_time VARCHAR(100) COMMENT '上映时间',
      category VARCHAR(100) COMMENT '分类',
      created_at TIMESTAMP DEFAULT current_timestamp,
      updated_at TIMESTAMP DEFAULT current_timestamp
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;

"""

images = """
    CREATE TABLE IF NOT EXISTS images(
      id INT PRIMARY KEY AUTO_INCREMENT,
      title VARCHAR(100) ,
      type VARCHAR(10) NOT NULL ,
      url TEXT NOT NULL ,
      is_upload BOOL DEFAULT FALSE 
    )ENGINE =InnoDB DEFAULT CHARSET=utf8;
"""

# def create_table():
# value = [('www.baidu.com', 'baidu'), ('www.baidu.com1', 'baidu1')]
# sql = 'INSERT INTO images (url,title) VALUE (%s , %s)'
# result = SQLHelper.execute(sql, value, True)

# print(result)


# SQLHelper.execute(movies)


# create_table()

# SQLHelper.execute('DROP TABLE images')
# SQLHelper.execute(images)
print(SQLHelper.fetch_one('SELECT * FROM images'))
