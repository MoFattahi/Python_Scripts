# OneHot Encoding Categorical Features
import pandas as pd
def encode_features(df_train , df_test , categorical_cols):
    # Method 1: (Encoding)
    encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)

    # reshape to 2D format
    df_train_values = df_train[categorical_cols].values.reshape(-1,1)
    df_test_values = df_test[categorical_cols].values.reshape(-1,1)
    
    f = lambda x: encoder.fit_transform(x)

    df_train_values = f(df_train_values)
    df_test_values = f(df_test_values)
    # reverse the reshape
    print(df_train_values.shape)
    print(df_train[categorical_cols].shape)
    df_train[categorical_cols] = df_train_values.reshape(df_train[categorical_cols].shape[0] , 6)
    df_test[categorical_cols] = df_test_values.reshape(df_test[categorical_cols].shape[0] , 6)


    encode_cols_train = pd.DataFrame(df_train[categorical_cols])
    encode_cols_test = pd.DataFrame(df_test[categorical_cols])

    encode_cols_train.index = df_train.index
    encode_cols_test.index = df_test.index

    column_name = encoder.get_feature_names([categorical_cols])
    encode_cols_train.columns = column_name
    encode_cols_test.columns = column_name
    
    other_data_train = df_train.drop(categorical_cols, axis=1)
    other_data_test = df_train.drop(categorical_cols, axis=1)

    df_new_train = pd.concat([other_data_train , encode_cols_train], axis=1)
    df_new_test = pd.concat([other_data_test , encode_cols_test], axis=1)

    return df_new_train , df_new_test




    # Method 2: (Encoding)
def encode_features(df_train , df_test , categorical_cols):
    OH_encoder = OneHotEncoder(handle_unknown='ignore' , sparse = False)

    # reshape to 2D format
    df_train_values = df_train[categorical_cols].values.reshape(-1,1)
    df_test_values = df_test[categorical_cols].values.reshape(-1,1)
    
    f = lambda x: OH_encoder.fit_transform(x)

    df_train_values = f(df_train_values)
    df_test_values = f(df_test_values)
    # reverse the reshape
    df_train[categorical_cols] = df_train_values.reshape(df_train[categorical_cols].shape[0] , 6)
    df_test[categorical_cols] = df_test_values.reshape(df_test[categorical_cols].shape[0] , 6)

    OH_cols_train = pd.DataFrame(df_train[categorical_cols])
    OH_cols_test = pd.DataFrame(df_test[categorical_cols])


    # One-hot encoding removed index; put it back
    OH_cols_train.index = df_train.index
    OH_cols_test.index = df_test.index

    # Remove categorical columns (will replace with one-hot encoding)
    num_X_train = df_train.drop(categorical_cols, axis=1)
    num_X_test = df_test.drop(categorical_cols, axis=1)

    # Add one-hot encoded columns to numerical features
    OH_df_train = pd.concat([num_X_train, OH_cols_train], axis=1)
    OH_df_test = pd.concat([num_X_test, OH_cols_test], axis=1) 

    return OH_df_train , OH_df_test