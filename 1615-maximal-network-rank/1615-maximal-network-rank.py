class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        city_to_cities = [ set() for i in range( n ) ]
        max_network_rank = 0
        for road in roads:
            city_to_cities[ road[0] ].add( road[1] )
            city_to_cities[ road[1] ].add( road[0] )
        for city_1 in range( n ):
            for city_2 in range( city_1 + 1, n ):
                network_rank = len( city_to_cities[city_1] ) + len( city_to_cities[city_2] )
                if ( city_1 in city_to_cities[city_2] ):
                    network_rank -= 1
                max_network_rank = max(max_network_rank, network_rank)
        return max_network_rank        