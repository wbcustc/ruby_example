class CreateEvents < ActiveRecord::Migration
  def change
    create_table :events do |t|
      t.string :title
      t.string :address
      t.datetime :event_at
      t.float :lat
      t.float :lng
      t.string :tags, array:true
      t.timestamps null: false
    end
  end
end
