Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      post 'users/new'
      post 'users/new/phone', to: 'users#new_with_phone_number'
      post 'users/validation', to: 'users#validation_code'
    end
  end
end
