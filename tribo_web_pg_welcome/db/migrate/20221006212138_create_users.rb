class CreateUsers < ActiveRecord::Migration[6.0]
  def change
    create_table :users do |t|
      t.string :username
      t.string :name
      t.string :first_name
      t.string :last_name
      t.string :email
      t.boolean :email_verified
      t.string :password
      t.string :phone_number
      t.boolean :phone_verified
      t.date :birth_day
      #t.references :address_id, null: false, foreign_key: true
      t.string :type
      t.boolean :verified_account

      t.timestamps
    end
  end
end
