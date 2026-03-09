"""
Centralized configuration for Project Capillary Siphon 2.0
All sensitive values loaded from environment variables
"""
import os
from typing import Dict, List
from dataclasses import dataclass
from dotenv import load_dotenv
import logging

load_dotenv()

@dataclass(frozen=True)
class ChainConfig:
    """Configuration for a single L2 chain"""
    name: str
    chain_id: int
    rpc_urls: List[str]  # Multiple RPCs for consensus
    explorer_api: str
    native_token: str
    gas_station_url: str
    private_mempool_rpc: str
    
@dataclass(frozen=True)
class AgentConfig:
    """Autonomous agent configuration"""
    agent_id: str
    private_key: str  # Loaded from secure storage
    heartbeat_interval: int = 30  # seconds
    max_gas_price_gwei: int = 50
    min_profit_threshold_usd: float = 0.50
    
@dataclass(frozen=True)
class BridgeConfig:
    """Cross-chain bridge endpoints"""
    socket_api: str = "https://api.socket.tech/v2"
    hop_api: str = "https://api.hop.exchange/v1"
    across_api: str = "https://across.to/api"
    
class Config:
    """Main configuration singleton"""
    
    # Chain configurations
    BASE = ChainConfig(
        name="Base",
        chain_id=8453,
        rpc_urls=[
            os.getenv("BASE_RPC_1", "https://mainnet.base.org"),
            os.getenv("BASE_RPC_2", "https://base.publicnode.com")
        ],
        explorer_api="https://api.basescan.org/api",
        native_token="ETH",
        gas_station_url="https://gasstation.base.org/v2",
        private_mempool_rpc="https://rpc.flashbots.net"
    )
    
    POLYGON = ChainConfig(
        name="Polygon",
        chain_id=137,
        rpc_urls=[
            os.getenv("POLYGON_RPC_1", "https://polygon-rpc.com"),
            os.getenv("POLYGON_RPC_2", "https://rpc-mainnet.maticvigil.com")
        ],
        explorer_api="https://api.polygonscan.com/api",
        native_token="MATIC",