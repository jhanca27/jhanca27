class User < ApplicationRecord
  # belongs_to :address_id
  has_one :token
end
