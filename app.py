import streamlit as st
import requests

# 高德地图API的基础URL
amap_api_base_url = 'https://restapi.amap.com/v3/geocode/geo'

# 你的API Key，请替换成你的实际Key
amap_api_key = '72b92e4ca894584ed2c6d8cab32ca303'  # 替换为你自己的API Key


def get_location_by_address(address):
    # 构建请求参数
    params = {
        'address': address,
        'key': amap_api_key,
        'output': 'json'
    }

    # 发送GET请求
    response = requests.get(amap_api_base_url, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        data = response.json()
        if 'geocodes' in data and data['geocodes']:
            geocode = data['geocodes'][0]
            location = geocode['location']
            return location
    else:
        return f"Error: {response.status_code}, {response.text}"


def main():
    # Streamlit 应用界面
    st.title("高德地图API查询")
    address = st.text_input("请输入地址:")

    if st.button("查询"):
        if address:
            location = get_location_by_address(address)
            if isinstance(location, str) and "Error" in location:
                st.error(location)
            else:
                st.success(f"经纬度: {location}")
        else:
            st.warning("请输入有效的地址！")


if __name__ == "__main__":
    main()