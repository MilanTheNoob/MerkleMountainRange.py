from mmr import MMR, MerkleProof

mmr = MMR()
pos1 = mmr.add(b"hello")
pos2 = mmr.add(b"world")

root = mmr.get_root()
proof = mmr.gen_proof(pos1)

# Serialize
mmr_json = mmr.serialize()
proof_json = proof.serialize()

# Deserialize
mmr2 = MMR.deserialize(mmr_json)
proof2 = MerkleProof.deserialize(proof_json)

# Verification still works
assert proof2.verify(mmr2.get_root(), pos1, b"hello")
assert not proof2.verify(mmr2.get_root(), pos1, b"world")

print(mmr2.serialize())
