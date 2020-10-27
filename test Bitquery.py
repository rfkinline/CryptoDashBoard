#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
import requests
import sys
import time
import datetime
from urllib.request import urlopen
import simplejson as json
#import json 
import requests
address='0x8998aC6F6d538207015F11E0aCfE7300FBa350E1'

def run_query(query):  # A simple function to use request$
	global address
	print(address)
	request = requests.post('https://graphql.bitquery.io/',	json = {"query":query, "variables":{"address": address}})
	if request.status_code == 200:
		return request.json()
	else:
		raise Exception('Query failed and return code is {}.{}'.format(request.status_code,query))
query = """query($address:String!){ethereum{address(address: {is: $address}){balances{currency{symbol, name,address}value}}}}"""
result = run_query(query)
b=json.dumps(result)
#b=("["+a+"]")
#print("b",b)
### TEST 1
b='[{"category":"DEXes","chain":"Ethereum","id":2,"name":"Uniswap","value":{"tvl":{"USD":{"value":2768984080,"relative_1d":1.75},"ETH":{"value":6863945,"relative_1d":1.76},"BTC":{"value":207470.33,"relative_1d":-0.19}},"total":{"USD":{"value":2768984080,"relative_1d":1.75},"ETH":{"value":3467708.5,"relative_1d":1.79},"BTC":{"value":27809.818,"relative_1d":2.77}},"balance":{"ERC20":{"DAI":{"value":2.0330728E8,"relative_1d":-4.37}}}},"contributesTo":null,"relative_1d":1.75,"timestamp":1603803600},{"category":"Lending","permissioning":"Open","variability":"Medium","website":"https://cdp.makerdao.com/","chain":"Ethereum","id":0,"name":"Maker","value":{"tvl":{"USD":{"value":2111777797,"relative_1d":0.06},"ETH":{"value":5234817.5,"relative_1d":0.07},"BTC":{"value":158228.16,"relative_1d":-1.85}},"total":{"USD":{"value":2111777797,"relative_1d":0.06},"ETH":{"value":2598558.8,"relative_1d":-0.12},"BTC":{"value":17219.172,"relative_1d":0.85}},"balance":{"ERC20":{"DAI":{"value":3.27752928E8,"relative_1d":-1.87}}}},"contributesTo":null,"relative_1d":0.06,"timestamp":1603803600},{"category":"Assets","chain":"Ethereum","id":5,"name":"WBTC","value":{"tvl":{"USD":{"value":1529077825,"relative_1d":3.05},"ETH":{"value":3790381.5,"relative_1d":3.06},"BTC":{"value":114568.48,"relative_1d":1.08}},"total":{"USD":{"value":1529077825,"relative_1d":3.05},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":114223.57,"relative_1d":0.88}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":3.05,"timestamp":1603803600},{"category":"Lending","permissioning":"Open","variability":"Medium","website":"https://compound.finance","chain":"Ethereum","id":1,"name":"Compound","value":{"tvl":{"USD":{"value":1078369360,"relative_1d":-0.12},"ETH":{"value":2673135,"relative_1d":-0.11},"BTC":{"value":80798.46,"relative_1d":-2.02}},"total":{"USD":{"value":1078369360,"relative_1d":-0.12},"ETH":{"value":1039855.56,"relative_1d":0.18},"BTC":{"value":15393.954,"relative_1d":4.14}},"balance":{"ERC20":{"DAI":{"value":3.32313984E8,"relative_1d":-1.87}}}},"contributesTo":null,"relative_1d":-0.12,"timestamp":1603803600},{"category":"Lending","variability":"medium","website":"https://aave.com","chain":"Ethereum","id":22,"name":"Aave","value":{"tvl":{"USD":{"value":997095002,"relative_1d":1.71},"ETH":{"value":2471666.5,"relative_1d":1.72},"BTC":{"value":74708.85,"relative_1d":-0.24}},"total":{"USD":{"value":997095002,"relative_1d":1.71},"ETH":{"value":458122.4,"relative_1d":1.47},"BTC":{"value":11352.505,"relative_1d":3.81}},"balance":{"ERC20":{"DAI":{"value":8280649.5,"relative_1d":-43.7}}}},"contributesTo":null,"relative_1d":1.71,"timestamp":1603803600},{"category":"DEXes","chain":"Ethereum","id":33,"name":"Curve Finance","value":{"tvl":{"USD":{"value":684337363,"relative_1d":3.65},"ETH":{"value":1696381.8,"relative_1d":3.66},"BTC":{"value":51275.016,"relative_1d":1.67}},"total":{"USD":{"value":684337363,"relative_1d":3.65},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":23976.262,"relative_1d":2.54}},"balance":{"ERC20":{"DAI":{"value":3.077782E7,"relative_1d":-16.35}}}},"contributesTo":null,"relative_1d":3.65,"timestamp":1603803600},{"category":"Derivatives","chain":"Ethereum","id":12,"name":"Synthetix","value":{"tvl":{"USD":{"value":572067258,"relative_1d":-0.87},"ETH":{"value":1418079,"relative_1d":-0.86},"BTC":{"value":42863.008,"relative_1d":-2.76}},"total":{"USD":{"value":572067258,"relative_1d":-0.87},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":-0.87,"timestamp":1603803600},{"category":"Assets","website":"https://harvest.finance","chain":"Ethereum","id":45,"name":"Harvest Finance","value":{"tvl":{"USD":{"value":416040576,"relative_1d":-24.36},"ETH":{"value":1031309.5,"relative_1d":-24.36},"BTC":{"value":31172.47,"relative_1d":-25.81}},"total":{"USD":{"value":416040576,"relative_1d":-24.36},"ETH":{"value":275143.28,"relative_1d":-21.47},"BTC":{"value":11383.757,"relative_1d":-17.05}},"balance":{"ERC20":{"DAI":{"value":1.7794606E7,"relative_1d":-34.64}}}},"contributesTo":null,"relative_1d":-24.36,"timestamp":1603803600},{"category":"Assets","chain":"Ethereum","id":30,"name":"RenVM","value":{"tvl":{"USD":{"value":345594223,"relative_1d":0.26},"ETH":{"value":856682.3,"relative_1d":0.27},"BTC":{"value":25894.172,"relative_1d":-1.66}},"total":{"USD":{"value":345594223,"relative_1d":0.26},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":22672.49,"relative_1d":-1.56}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":0.26,"timestamp":1603803600},{"category":"Assets","chain":"Ethereum","id":36,"name":"yearn.finance","value":{"tvl":{"USD":{"value":337989727,"relative_1d":1.68},"ETH":{"value":837831.8,"relative_1d":1.69},"BTC":{"value":25324.393,"relative_1d":-0.26}},"total":{"USD":{"value":337989727,"relative_1d":1.68},"ETH":{"value":57856.797,"relative_1d":-0.71},"BTC":{"value":2.018337,"relative_1d":1}},"balance":{"ERC20":{"DAI":{"value":3.790604E7,"relative_1d":-3.06}}}},"contributesTo":["Curve","Aave"],"relative_1d":1.68,"timestamp":1603803600},{"category":"DEXes","chain":"Ethereum","id":28,"name":"Balancer","value":{"tvl":{"USD":{"value":314207828,"relative_1d":-2.22},"ETH":{"value":778879.6,"relative_1d":-2.21},"BTC":{"value":23542.498,"relative_1d":-4.08}},"total":{"USD":{"value":314207828,"relative_1d":-2.22},"ETH":{"value":264360.34,"relative_1d":-0.98},"BTC":{"value":2443.9846,"relative_1d":1.95}},"balance":{"ERC20":{"DAI":{"value":4048642,"relative_1d":-1.89}}}},"contributesTo":null,"relative_1d":-2.22,"timestamp":1603803600},{"category":"DEXes","chain":"Ethereum","id":43,"name":"SushiSwap","value":{"tvl":{"USD":{"value":262296313,"relative_1d":2.29},"ETH":{"value":650197.9,"relative_1d":2.3},"BTC":{"value":19652.95,"relative_1d":0.34}},"total":{"USD":{"value":262296313,"relative_1d":2.29},"ETH":{"value":337980.1,"relative_1d":2.7},"BTC":{"value":300.68427,"relative_1d":-7.45}},"balance":{"ERC20":{"DAI":{"value":1.6315041E7,"relative_1d":-1.22}}}},"contributesTo":null,"relative_1d":2.29,"timestamp":1603803600},{"category":"Lending","chain":"Ethereum","id":13,"name":"InstaDApp","value":{"tvl":{"USD":{"value":200674919,"relative_1d":-1.17},"ETH":{"value":497446.56,"relative_1d":-1.16},"BTC":{"value":15035.872,"relative_1d":-3.06}},"total":{"USD":{"value":200674919,"relative_1d":-1.17},"ETH":{"value":164742.77,"relative_1d":-0.03},"BTC":{"value":96.61391,"relative_1d":0}},"balance":{"ERC20":{"DAI":{"value":6.0489836E7,"relative_1d":-5.95}}}},"contributesTo":["Maker","Compound"],"relative_1d":-1.17,"timestamp":1603803600},{"category":"Lending","permissioning":"Open","variability":"Medium","website":"https://cream.finance","chain":"Ethereum","id":42,"name":"C.R.E.A.M. Finance","value":{"tvl":{"USD":{"value":152677415,"relative_1d":4.91},"ETH":{"value":378467.1,"relative_1d":4.92},"BTC":{"value":11439.587,"relative_1d":2.9}},"total":{"USD":{"value":152677415,"relative_1d":4.91},"ETH":{"value":47056.066,"relative_1d":23.64},"BTC":{"value":1111.1057,"relative_1d":0.79}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":4.91,"timestamp":1603803600},{"category":"Payments","website":"https://flexa.network","chain":"Ethereum","id":31,"name":"Flexa","value":{"tvl":{"USD":{"value":84271854,"relative_1d":-0.17},"ETH":{"value":208898.77,"relative_1d":-0.16},"BTC":{"value":6314.1963,"relative_1d":-2.07}},"total":{"USD":{"value":84271854,"relative_1d":-0.17},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":-0.17,"timestamp":1603803600},{"category":"Derivatives","chain":"Ethereum","id":17,"name":"Nexus Mutual","value":{"tvl":{"USD":{"value":78639300,"relative_1d":-0.65},"ETH":{"value":194936.42,"relative_1d":-0.64},"BTC":{"value":5892.169,"relative_1d":-2.55}},"total":{"USD":{"value":78639300,"relative_1d":-0.65},"ETH":{"value":193911.8,"relative_1d":-0.51},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":382193.84,"relative_1d":0.05}}}},"contributesTo":null,"relative_1d":-0.65,"timestamp":1603803600},{"category":"Assets","chain":"Ethereum","id":25,"name":"dForce","value":{"tvl":{"USD":{"value":75655001,"relative_1d":-1.94},"ETH":{"value":187538.73,"relative_1d":-1.93},"BTC":{"value":5668.5654,"relative_1d":-3.81}},"total":{"USD":{"value":75655001,"relative_1d":-1.94},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":5095498.5,"relative_1d":-0.39}}}},"contributesTo":null,"relative_1d":-1.94,"timestamp":1603803600},{"category":"Assets","chain":"Ethereum","id":34,"name":"mStable","value":{"tvl":{"USD":{"value":41744402,"relative_1d":-0.73},"ETH":{"value":103478.85,"relative_1d":-0.72},"BTC":{"value":3127.7627,"relative_1d":-2.63}},"total":{"USD":{"value":41744402,"relative_1d":-0.73},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":87.24275,"relative_1d":7534.46}}}},"contributesTo":null,"relative_1d":-0.73,"timestamp":1603803600},{"category":"Lending","permissioning":"Open","variability":"Medium","website":"https://dydx.exchange/","chain":"Ethereum","id":11,"name":"dYdX","value":{"tvl":{"USD":{"value":30483457,"relative_1d":-1.71},"ETH":{"value":75564.45,"relative_1d":-1.7},"BTC":{"value":2284.0193,"relative_1d":-3.59}},"total":{"USD":{"value":30483457,"relative_1d":-1.71},"ETH":{"value":49789.285,"relative_1d":-17.74},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":1608548.5,"relative_1d":-8.05}}}},"contributesTo":null,"relative_1d":-1.71,"timestamp":1603803600},{"category":"Assets","chain":"Ethereum","id":18,"name":"Set Protocol","value":{"tvl":{"USD":{"value":29750753,"relative_1d":0.29},"ETH":{"value":73748.18,"relative_1d":0.3},"BTC":{"value":2229.1204,"relative_1d":-1.62}},"total":{"USD":{"value":29750753,"relative_1d":0.29},"ETH":{"value":28363.695,"relative_1d":-3.93},"BTC":{"value":265.97485,"relative_1d":18.92}},"balance":{"ERC20":{"DAI":{"value":926716.7,"relative_1d":0.03}}}},"contributesTo":null,"relative_1d":0.29,"timestamp":1603803600},{"category":"DEXes","chain":"Ethereum","id":44,"name":"DODO","value":{"tvl":{"USD":{"value":28295890,"relative_1d":-1.03},"ETH":{"value":70141.766,"relative_1d":-1.02},"BTC":{"value":2120.1125,"relative_1d":-2.92}},"total":{"USD":{"value":28295890,"relative_1d":-1.03},"ETH":{"value":17902.598,"relative_1d":-2.04},"BTC":{"value":238.65886,"relative_1d":16.24}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":-1.03,"timestamp":1603803600},{"category":"Lending","permissioning":"Open","variability":"Medium","website":"https://for.tube","chain":"Ethereum","id":40,"name":"ForTube","value":{"tvl":{"USD":{"value":27739193,"relative_1d":-18.09},"ETH":{"value":68761.79,"relative_1d":-18.09},"BTC":{"value":2078.4011,"relative_1d":-19.66}},"total":{"USD":{"value":27739193,"relative_1d":-18.09},"ETH":{"value":13336.405,"relative_1d":-34.15},"BTC":{"value":109.43665,"relative_1d":531.24}},"balance":{"ERC20":{"DAI":{"value":93195.24,"relative_1d":0}}}},"contributesTo":null,"relative_1d":-18.09,"timestamp":1603803600},{"category":"DEXes","chain":"Ethereum","id":26,"name":"Loopring","value":{"tvl":{"USD":{"value":16194600,"relative_1d":2.16},"ETH":{"value":40144.27,"relative_1d":2.17},"BTC":{"value":1213.4049,"relative_1d":0.21}},"total":{"USD":{"value":16194600,"relative_1d":2.16},"ETH":{"value":14923.142,"relative_1d":-0.13},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":186078.75,"relative_1d":-0.03}}}},"contributesTo":null,"relative_1d":2.16,"timestamp":1603803600},{"category":"DEXes","chain":"Ethereum","id":14,"name":"Bancor","value":{"tvl":{"USD":{"value":13895764,"relative_1d":-3.45},"ETH":{"value":34445.76,"relative_1d":-3.44},"BTC":{"value":1041.1611,"relative_1d":-5.3}},"total":{"USD":{"value":13895764,"relative_1d":-3.45},"ETH":{"value":12051.425,"relative_1d":-2.38},"BTC":{"value":0.015684,"relative_1d":0}},"balance":{"ERC20":{"DAI":{"value":222533.53,"relative_1d":-3.08}}}},"contributesTo":null,"relative_1d":-3.45,"timestamp":1603803600},{"category":"Payments","chain":"Bitcoin","id":3,"name":"Lightning Network","value":{"tvl":{"USD":{"value":13865201,"relative_1d":1.64},"ETH":{"value":34370,"relative_1d":1.65},"BTC":{"value":1038.8712,"relative_1d":-0.3}},"total":{"USD":{"value":13865201,"relative_1d":1.64},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":1040.56,"relative_1d":0.08}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":1.64,"timestamp":1603803600},{"category":"Assets","website":"https://metronome.io","chain":"Ethereum","id":37,"name":"Metronome","value":{"tvl":{"USD":{"value":11089680,"relative_1d":0.35},"ETH":{"value":27489.85,"relative_1d":0.36},"BTC":{"value":830.9111,"relative_1d":-1.57}},"total":{"USD":{"value":11089680,"relative_1d":0.35},"ETH":{"value":16989.078,"relative_1d":-0.04},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":0.35,"timestamp":1603803600},{"category":"DEXes","chain":"Ethereum","id":6,"name":"Kyber","value":{"tvl":{"USD":{"value":9426556,"relative_1d":-3.23},"ETH":{"value":23367.186,"relative_1d":-3.22},"BTC":{"value":706.299,"relative_1d":-5.07}},"total":{"USD":{"value":9426556,"relative_1d":-3.23},"ETH":{"value":5482.3213,"relative_1d":-3.14},"BTC":{"value":97.38338,"relative_1d":-0.72}},"balance":{"ERC20":{"DAI":{"value":681053.7,"relative_1d":-48.28}}}},"contributesTo":null,"relative_1d":-3.23,"timestamp":1603803600},{"category":"DEXes","chain":"Ethereum","id":39,"name":"Gnosis","value":{"tvl":{"USD":{"value":5102879,"relative_1d":0.29},"ETH":{"value":12649.361,"relative_1d":0.3},"BTC":{"value":382.34094,"relative_1d":-1.63}},"total":{"USD":{"value":5102879,"relative_1d":0.29},"ETH":{"value":3577.5388,"relative_1d":1.5},"BTC":{"value":0.111844,"relative_1d":0}},"balance":{"ERC20":{"DAI":{"value":815978.06,"relative_1d":2.09}}}},"contributesTo":null,"relative_1d":0.29,"timestamp":1603803600},{"category":"Payments","chain":"Ethereum","id":9,"name":"xDai","value":{"tvl":{"USD":{"value":4954918,"relative_1d":-2.61},"ETH":{"value":12282.586,"relative_1d":-2.6},"BTC":{"value":371.25473,"relative_1d":-4.47}},"total":{"USD":{"value":4954918,"relative_1d":-2.61},"ETH":{"value":1621.6619,"relative_1d":0.66},"BTC":{"value":1.65534,"relative_1d":-0.6}},"balance":{"ERC20":{"DAI":{"value":2705709.5,"relative_1d":-3.35}}}},"contributesTo":null,"relative_1d":-2.61,"timestamp":1603803600},{"category":"DEXes","chain":"Ethereum","id":29,"name":"DeversiFi","value":{"tvl":{"USD":{"value":3601096,"relative_1d":-9.11},"ETH":{"value":8926.641,"relative_1d":-9.1},"BTC":{"value":269.81757,"relative_1d":-10.85}},"total":{"USD":{"value":3601096,"relative_1d":-9.11},"ETH":{"value":2083.6094,"relative_1d":-2.25},"BTC":{"value":72.04648,"relative_1d":0}},"balance":{"ERC20":{"DAI":{"value":47108.297,"relative_1d":-84.3}}}},"contributesTo":null,"relative_1d":-9.11,"timestamp":1603803600},{"category":"Derivatives","chain":"Ethereum","id":23,"name":"Erasure","value":{"tvl":{"USD":{"value":3548948,"relative_1d":-2.21},"ETH":{"value":8797.372,"relative_1d":-2.2},"BTC":{"value":265.9103,"relative_1d":-4.07}},"total":{"USD":{"value":3548948,"relative_1d":-2.21},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":5505.221,"relative_1d":0}}}},"contributesTo":null,"relative_1d":-2.21,"timestamp":1603803600},{"category":"Assets","chain":"Ethereum","id":35,"name":"PieDAO","value":{"tvl":{"USD":{"value":2623390,"relative_1d":0.14},"ETH":{"value":6503.0366,"relative_1d":0.15},"BTC":{"value":196.56148,"relative_1d":-1.77}},"total":{"USD":{"value":2623390,"relative_1d":0.14},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":19.100552,"relative_1d":0}},"balance":{"ERC20":{"DAI":{"value":14088.133,"relative_1d":0}}}},"contributesTo":null,"relative_1d":0.14,"timestamp":1603803600},{"category":"Lending","chain":"Ethereum","id":21,"name":"DDEX","value":{"tvl":{"USD":{"value":2576280,"relative_1d":-2.84},"ETH":{"value":6386.2573,"relative_1d":-2.83},"BTC":{"value":193.03168,"relative_1d":-4.7}},"total":{"USD":{"value":2576280,"relative_1d":-2.84},"ETH":{"value":3203.785,"relative_1d":-4.25},"BTC":{"value":20.84681,"relative_1d":-17.59}},"balance":{"ERC20":{"DAI":{"value":38750.324,"relative_1d":0}}}},"contributesTo":null,"relative_1d":-2.84,"timestamp":1603803600},{"category":"Derivatives","chain":"Ethereum","id":27,"name":"Opyn","value":{"tvl":{"USD":{"value":2188912,"relative_1d":2.38},"ETH":{"value":5426.023,"relative_1d":2.39},"BTC":{"value":164.00755,"relative_1d":0.43}},"total":{"USD":{"value":2188912,"relative_1d":2.38},"ETH":{"value":1902.7325,"relative_1d":2.42},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":1.801998,"relative_1d":0}}}},"contributesTo":null,"relative_1d":2.38,"timestamp":1603803600},{"category":"Assets","chain":"Ethereum","id":16,"name":"Melon","value":{"tvl":{"USD":{"value":1819423,"relative_1d":0.23},"ETH":{"value":4510.109,"relative_1d":0.24},"BTC":{"value":136.32303,"relative_1d":-1.69}},"total":{"USD":{"value":1819423,"relative_1d":0.23},"ETH":{"value":2052.0986,"relative_1d":-0.29},"BTC":{"value":25.48912,"relative_1d":0.67}},"balance":{"ERC20":{"DAI":{"value":34908.273,"relative_1d":-0.62}}}},"contributesTo":null,"relative_1d":0.23,"timestamp":1603803600},{"category":"Derivatives","website":"https://mcdex.io","chain":"Ethereum","id":32,"name":"MCDEX","value":{"tvl":{"USD":{"value":1524863,"relative_1d":0},"ETH":{"value":3779.9336,"relative_1d":0.01},"BTC":{"value":114.25267,"relative_1d":-1.9}},"total":{"USD":{"value":1524863,"relative_1d":0},"ETH":{"value":3603.8394,"relative_1d":0.12},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":0,"timestamp":1603803600},{"category":"Lending","chain":"Ethereum","id":24,"name":"Robo-Advisor for Yield","shortName":"RAY","value":{"tvl":{"USD":{"value":802554,"relative_1d":0.21},"ETH":{"value":1989.4252,"relative_1d":0.22},"BTC":{"value":60.132576,"relative_1d":-1.7}},"total":{"USD":{"value":802554,"relative_1d":0.21},"ETH":{"value":279.03088,"relative_1d":0.01},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":233495.2,"relative_1d":-0.36}}}},"contributesTo":null,"relative_1d":0.21,"timestamp":1603803600},{"category":"Derivatives","chain":"Ethereum","id":4,"name":"Augur","value":{"tvl":{"USD":{"value":636663,"relative_1d":-0.2},"ETH":{"value":1578.2034,"relative_1d":-0.19},"BTC":{"value":47.70294,"relative_1d":-2.1}},"total":{"USD":{"value":636663,"relative_1d":-0.2},"ETH":{"value":1581.145,"relative_1d":0},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":-0.2,"timestamp":1603803600},{"category":"Lending","permissioning":"Open","website":"https://bzx.network/","chain":"Ethereum","id":19,"name":"bZx","value":{"tvl":{"USD":{"value":235558,"relative_1d":-0.26},"ETH":{"value":583.9171,"relative_1d":-0.25},"BTC":{"value":17.64954,"relative_1d":-2.17}},"total":{"USD":{"value":235558,"relative_1d":-0.26},"ETH":{"value":463.8651,"relative_1d":0},"BTC":{"value":0.03368273,"relative_1d":0}},"balance":{"ERC20":{"DAI":{"value":32488.955,"relative_1d":0}}}},"contributesTo":null,"relative_1d":-0.26,"timestamp":1603803600},{"category":"Derivatives","chain":"Ethereum","id":38,"name":"ACO","value":{"tvl":{"USD":{"value":178544,"relative_1d":15.67},"ETH":{"value":442.58694,"relative_1d":15.68},"BTC":{"value":13.37768,"relative_1d":13.46}},"total":{"USD":{"value":178544,"relative_1d":15.67},"ETH":{"value":238.53726,"relative_1d":19.28},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":15.67,"timestamp":1603803600},{"category":"Lending","chain":"Ethereum","id":7,"name":"Dharma","value":{"tvl":{"USD":{"value":151376,"relative_1d":-0.18},"ETH":{"value":375.24106,"relative_1d":-0.17},"BTC":{"value":11.342076,"relative_1d":-2.08}},"total":{"USD":{"value":151376,"relative_1d":-0.18},"ETH":{"value":346.65253,"relative_1d":0},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":9025.319,"relative_1d":0}}}},"contributesTo":["Compound"],"relative_1d":-0.18,"timestamp":1603803600},{"category":"Derivatives","chain":"Ethereum","id":41,"name":"Opium Network","value":{"tvl":{"USD":{"value":79515,"relative_1d":-0.12},"ETH":{"value":197.10716,"relative_1d":-0.11},"BTC":{"value":5.957782,"relative_1d":-2.03}},"total":{"USD":{"value":79515,"relative_1d":-0.12},"ETH":{"value":178.65857,"relative_1d":0},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":6578.8794,"relative_1d":0}}}},"contributesTo":null,"relative_1d":-0.12,"timestamp":1603803600},{"category":"Derivatives","chain":"Ethereum","id":8,"name":"Veil","value":{"tvl":{"USD":{"value":50539,"relative_1d":-0.2},"ETH":{"value":125.279495,"relative_1d":-0.19},"BTC":{"value":3.7867112,"relative_1d":-2.1}},"total":{"USD":{"value":50539,"relative_1d":-0.2},"ETH":{"value":125.513855,"relative_1d":0},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":null,"relative_1d":null}}}},"contributesTo":null,"relative_1d":-0.2,"timestamp":1603803600},{"category":"Payments","chain":"Ethereum","id":15,"name":"Connext","value":{"tvl":{"USD":{"value":12881,"relative_1d":-0.03},"ETH":{"value":31.930294,"relative_1d":-0.02},"BTC":{"value":0.9651284,"relative_1d":-1.94}},"total":{"USD":{"value":12881,"relative_1d":-0.03},"ETH":{"value":null,"relative_1d":null},"BTC":{"value":null,"relative_1d":null}},"balance":{"ERC20":{"DAI":{"value":12768.952,"relative_1d":0}}}},"contributesTo":null,"relative_1d":-0.03,"timestamp":1603803600}]'
b=json.loads(b)
#print (b)
for row in b:
#	print(row)
        name = row["value"]["tvl"]["USD"]["value"]
        print("bbbbbbbbbbbbbbbbbbb",name)

### Test 2
c='{"originalRequest":{"category":{}},"totalResultSize":209,"products":[{"id":"1000004006560322","ean":"0828768235928","gpc":"music","title":"title","specsTag":"tag","summary":"summary","rating":45,"urls":[{"key":"DESKTOP","value":"http://www.url.com"},{"key":"MOBILE","value":"https://m.url.com"}]}]}'
c=json.loads(c)
#print ("c",c)
for row in c["products"][0]["urls"]:
#for row in b
	name = row["value"]
	print(name)




#	if name == 'WBTC':
#		WBTC = row['value']['tvl']['BTC']
#		print(WBTC)
#	symbol = row["symbol"]
#	value = str(row("value"))
#	print(token_symbol, value)
#	print(symbol)
#	print('Result - {}'.format(row["data"],["ethereum"],["address"],["balances"],["currency"],["symbol"]))
#print (result["data"]["ethereum"]["address"]["balances"]["currency"][1])
#	print ( 'Result - {}'.format(result))

#extracted_recipes = []
#for recipe in result:
#  extracted_recipes.append({
#            'symbol': recipe['currency']['symbol'],
#            'value': recipe(['balances']['value'])        })
#  print (extracted_recipes)
#  print (recipe)











