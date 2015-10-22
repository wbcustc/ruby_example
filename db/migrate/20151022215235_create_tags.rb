class CreateTags < ActiveRecord::Migration
  def change
    create_table :tags do |t|
      t.string :tag_name
      t.string :photo_url

      t.timestamps null: false
    end
  end
end
