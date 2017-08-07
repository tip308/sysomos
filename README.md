# sysomos
A simple wrapper for Sysomos API

## Quick Start

### Usage

#### Prerequisites

This module requires `requests` to be installed

#### Authentication

Import module and initate a client:
```
import sysomos
client = sysomos.twitter(api_key='abcd1234...')
```

#### Searching for profile information:
```
client.profiles(handles=['Sysomos','Twitter'])
```
